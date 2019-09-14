using System;
using System.Reflection;
using System.Collections.Generic;
using System.IO;

namespace PyStubblerLib
{
  public static class StubBuilder
  {
    private static List<string> SearchPaths { get; set; } = new List<string>();

    public static string BuildAssemblyStubs(string targetAssemblyPath, string destPath = null, string[] searchPaths = null, BuildConfig cfgs = null)
    {
      // prepare configs
      if (cfgs is null)
        cfgs = new BuildConfig();

      // prepare resolver
      AppDomain.CurrentDomain.AssemblyResolve += AssemblyResolve; ;

      // pick a dll and load
      Assembly assemblyToStub = Assembly.LoadFrom(targetAssemblyPath);
      SearchPaths.Add(targetAssemblyPath);
      if (searchPaths != null)
        SearchPaths.AddRange(searchPaths);

      // extract types
      Type[] typesToStub = assemblyToStub.GetExportedTypes();
      string rootNamespace = typesToStub[0].Namespace.Split('.')[0];

      // prepare output directory
      DirectoryInfo stubsDirectory;
      if (cfgs.DestPathIsRoot && Directory.Exists(destPath))
      {
        stubsDirectory = new DirectoryInfo(destPath);
      }
      else
      {
        var extendedRootNS = cfgs.Prefix + rootNamespace + cfgs.Postfix;
        if (destPath is null || !Directory.Exists(destPath))
          stubsDirectory = Directory.CreateDirectory(extendedRootNS);
        else
          stubsDirectory = Directory.CreateDirectory(Path.Combine(destPath, extendedRootNS));
      }

      // build type db
      var stubDictionary = new Dictionary<string, List<Type>>();
      foreach (var stubType in typesToStub)
      {
        if (!stubDictionary.ContainsKey(stubType.Namespace))
          stubDictionary[stubType.Namespace] = new List<Type>();
        stubDictionary[stubType.Namespace].Add(stubType);
      }

      // generate stubs for each type
      foreach (var stubList in stubDictionary.Values)
        WriteStubList(stubsDirectory, stubList);

      return stubsDirectory.FullName;
    }

    private static Assembly AssemblyResolve(object sender, ResolveEventArgs args)
    {
      string assemblyToResolve = args.Name.Substring(0, args.Name.IndexOf(',')) + ".dll";

      // try to find the dll in given search paths
      foreach (var searchPath in SearchPaths)
      {
        string assemblyPath = Path.Combine(searchPath, assemblyToResolve);
        if (File.Exists(assemblyPath))
          return Assembly.LoadFrom(assemblyPath);
      }

      // say i don't know
      return null;
    }

    private static void WriteStubList(DirectoryInfo rootDirectory, List<Type> stubTypes)
    {
      string[] ns = stubTypes[0].Namespace.Split('.');
      string path = rootDirectory.FullName;
      for (int i = 1; i < ns.Length; i++)
        path = Path.Combine(path, ns[i]);

      if (!Directory.Exists(path))
        Directory.CreateDirectory(path);

      path = Path.Combine(path, "__init__.pyi");

      var sb = new System.Text.StringBuilder();
      sb.AppendLine("from typing import Tuple, Set, Iterable, List");

      foreach (var stubType in stubTypes)
      {
        sb.AppendLine();
        sb.AppendLine();
        if (stubType.IsGenericType)
          continue; //skip generics for now
        if (stubType.IsEnum)
        {
          sb.AppendLine($"class {stubType.Name}:");
          var names = Enum.GetNames(stubType);
          var values = Enum.GetValues(stubType);
          for (int i = 0; i < names.Length; i++)
          {
            string name = names[i];
            if (name.Equals("None", StringComparison.Ordinal))
              name = $"#{name}";

            object val = Convert.ChangeType(values.GetValue(i), Type.GetTypeCode(stubType));
            sb.AppendLine($"    {name} = {val}");
          }
          continue;
        }

        if (stubType.BaseType != null &&
          stubType.BaseType.FullName.StartsWith(ns[0]) &&
          stubType.BaseType.FullName.IndexOf('+') < 0 &&
          stubType.BaseType.FullName.IndexOf('`') < 0
          )
          sb.AppendLine($"class {stubType.Name}({stubType.BaseType.Name}):");
        else
          sb.AppendLine($"class {stubType.Name}:");

        // constructors
        ConstructorInfo[] constructors = stubType.GetConstructors();
        foreach (var constructor in constructors)
        {
          if (constructors.Length > 1)
            sb.AppendLine("    @overload");
          sb.Append("    def __init__(self");
          var parameters = constructor.GetParameters();
          for (int i = 0; i < parameters.Length; i++)
          {
            if (0 == i)
              sb.Append(", ");
            sb.Append($"{SafePythonName(parameters[i].Name)}: {ToPythonType(parameters[i].ParameterType)}");
            if (i < (parameters.Length - 1))
              sb.Append(", ");
          }
          sb.AppendLine("): ...");
        }

        // methods
        MethodInfo[] methods = stubType.GetMethods();
        Dictionary<string, int> methodNames = new Dictionary<string, int>();
        foreach (var method in methods)
        {
          int count;
          if (methodNames.TryGetValue(method.Name, out count))
            count++;
          else
            count = 1;
          methodNames[method.Name] = count;
        }

        foreach (var method in methods)
        {
          if (method.DeclaringType != stubType)
            continue;
          var parameters = method.GetParameters();
          int outParamCount = 0;
          int refParamCount = 0;
          foreach (var p in parameters)
          {
            if (p.IsOut)
              outParamCount++;
            else if (p.ParameterType.IsByRef)
              refParamCount++;
          }
          int parameterCount = parameters.Length - outParamCount;

          if (method.IsSpecialName && (method.Name.StartsWith("get_") || method.Name.StartsWith("set_")))
          {
            string propName = method.Name.Substring("get_".Length);
            if (method.Name.StartsWith("get_"))
              sb.AppendLine("    @property");
            else
            {
              sb.AppendLine($"    @{propName}.setter");
            }
            sb.Append($"    def {propName}(");
          }
          else
          {
            if (methodNames[method.Name] > 1)
              sb.AppendLine("    @overload");
            sb.Append($"    def {method.Name}(");
          }

          bool addComma = false;
          if (!method.IsStatic)
          {
            sb.Append("self");
            addComma = true;
          }
          for (int i = 0; i < parameters.Length; i++)
          {
            if (parameters[i].IsOut)
              continue;

            if (addComma)
              sb.Append(", ");

            sb.Append($"{SafePythonName(parameters[i].Name)}: {ToPythonType(parameters[i].ParameterType)}");
            addComma = true;
          }
          sb.Append(")");
          {
            List<string> types = new List<string>();
            if (method.ReturnType == typeof(void))
            {
              if (outParamCount == 0 && refParamCount == 0)
                types.Add("None");
            }
            else
              types.Add(ToPythonType(method.ReturnType));

            foreach (var p in parameters)
            {
              if (p.IsOut || (p.ParameterType.IsByRef))
              {
                types.Add(ToPythonType(p.ParameterType));
              }
            }

            sb.Append($" -> ");
            if (outParamCount == 0 && refParamCount == 0)
              sb.Append(types[0]);
            else
            {
              sb.Append("Tuple[");
              for (int i = 0; i < types.Count; i++)
              {
                if (i > 0)
                  sb.Append(", ");
                sb.Append(types[i]);
              }
              sb.Append("]");
            }
          }
          sb.AppendLine(": ...");
        }
      }
      File.WriteAllText(path, sb.ToString());
    }

    private static string SafePythonName(string s)
    {
      if (s == "from")
        return "from_";
      return s;
    }

    private static string ToPythonType(string s)
    {
      string rc = s;
      if (rc.EndsWith("&"))
        rc = rc.Substring(0, rc.Length - 1);

      if (rc.EndsWith("`1") || rc.EndsWith("`2"))
        rc = rc.Substring(0, rc.Length - 2);

      if (rc.EndsWith("[]"))
      {
        string partial = ToPythonType(rc.Substring(0, rc.Length - 2));
        return $"Set({partial})";
      }

      if (rc.EndsWith("*"))
        return rc.Substring(0, rc.Length - 1); // ? not sure what we can do for pointers

      if (rc.Equals("String"))
        return "str";
      if (rc.Equals("Double"))
        return "float";
      if (rc.Equals("Boolean"))
        return "bool";
      if (rc.Equals("Int32"))
        return "int";
      return rc;
    }

    private static string ToPythonType(Type t)
    {
      if (t.IsGenericType && t.Name.StartsWith("IEnumerable"))
      {
        string rc = ToPythonType(t.GenericTypeArguments[0]);
        return $"Iterable[{rc}]";
      }
      // TODO: Figure out the right way to get at IEnumerable<T>
      if (t.FullName != null && t.FullName.StartsWith("System.Collections.Generic.IEnumerable`1[["))
      {
        string enumerableType = t.FullName.Substring("System.Collections.Generic.IEnumerable`1[[".Length);
        enumerableType = enumerableType.Substring(0, enumerableType.IndexOf(','));
        var pieces = enumerableType.Split('.');
        string rc = ToPythonType(pieces[pieces.Length - 1]);
        return $"Iterable[{rc}]";
      }
      if (t.FullName != null && t.FullName.StartsWith("System.Collections.Generic.IList`1[["))
      {
        string enumerableType = t.FullName.Substring("System.Collections.Generic.IList`1[[".Length);
        enumerableType = enumerableType.Substring(0, enumerableType.IndexOf(','));
        var pieces = enumerableType.Split('.');
        string rc = ToPythonType(pieces[pieces.Length - 1]);
        return $"List[{rc}]";
      }
      return ToPythonType(t.Name);
    }
  }
}
