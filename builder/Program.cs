using System;
using System.Reflection;
using System.Collections.Generic;

namespace PythonStubsBuilder
{
  class Program
  {
    static string AssemblyPath { get; set; }

    static void Main(string[] args)
    {
      string[] dllsToStub = new string[] {
        @"C:\Program Files\Rhino WIP\System\Eto.dll",
        @"C:\Program Files\Rhino WIP\System\RhinoCommon.dll",
        @"C:\Program Files\Rhino WIP\Plug-ins\Grasshopper\Grasshopper.dll",
        @"C:\Program Files\Rhino WIP\Plug-ins\Grasshopper\GH_IO.dll",
        @"C:\Program Files\Rhino WIP\Plug-ins\Grasshopper\GH_Util.dll" };

      // allow command line list of files to stub instead of the build-in list
      if (args.Length > 0)
        dllsToStub = args;

      for (int i = 0; i < dllsToStub.Length; i++)
      {
        AssemblyPath = dllsToStub[i];
        AppDomain.CurrentDomain.AssemblyResolve += AssemblyResolve;
        Assembly assemblyToStub = Assembly.LoadFrom(AssemblyPath);
        Type[] typesToStub = assemblyToStub.GetExportedTypes();
        string rootNamespace = typesToStub[0].Namespace.Split('.')[0];
        var stubsDirectory = System.IO.Directory.CreateDirectory($"{rootNamespace}-stubs");
        var stubDictionary = new Dictionary<string, List<Type>>();

        foreach (var stubType in typesToStub)
        {
          if (!stubDictionary.ContainsKey(stubType.Namespace))
            stubDictionary[stubType.Namespace] = new List<Type>();
          stubDictionary[stubType.Namespace].Add(stubType);
        }

        foreach (var stubList in stubDictionary.Values)
        {
          WriteStubList(stubsDirectory, stubList);
        }
        var keys = stubDictionary.Keys;
        Console.WriteLine($"{dllsToStub[i]} - version {assemblyToStub.GetName().Version}");
      }
    }

    private static Assembly AssemblyResolve(object sender, ResolveEventArgs args)
    {
      string assemblyToResolve = args.Name.Substring(0, args.Name.IndexOf(',')) + ".dll";
      {
        string dirName = System.IO.Path.GetDirectoryName(AssemblyPath);
        int index = dirName.IndexOf("\\Rhino");
        if( index > 0)
        {
          index = dirName.IndexOf("\\", index + 1);
          string rhinoDir = dirName.Substring(0, index + 1);
          string rhinoCommonPath = System.IO.Path.Combine(rhinoDir, "System", assemblyToResolve);
          if (System.IO.File.Exists(rhinoCommonPath))
            return Assembly.LoadFrom(rhinoCommonPath);
        }

      }
      return null;
    }

    private static void WriteStubList(System.IO.DirectoryInfo rootDirectory, List<Type> stubTypes)
    {
      string[] ns = stubTypes[0].Namespace.Split('.');
      string path = rootDirectory.FullName;
      for (int i = 1; i < ns.Length; i++)
        path = System.IO.Path.Combine(path, ns[i]);

      if (!System.IO.Directory.Exists(path))
        System.IO.Directory.CreateDirectory(path);

      path = System.IO.Path.Combine(path, "__init__.pyi");

      var sb = new System.Text.StringBuilder();
      sb.AppendLine("from typing import Tuple, Set, Iterable, List");
      sb.AppendLine();
      foreach(var stubType in stubTypes)
      {
        if (stubType.IsGenericType)
          continue; //skip generics for now
        if (stubType.IsEnum)
        {
          sb.AppendLine($"class {stubType.Name}:");
          var names = Enum.GetNames(stubType);
          var values = Enum.GetValues(stubType);
          for(int i=0; i<names.Length; i++)
          {
            object val = Convert.ChangeType(values.GetValue(i), Type.GetTypeCode(stubType));
            sb.AppendLine($"    {names[i]} = {val}");
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
        foreach(var constructor in stubType.GetConstructors())
        {
          var parameters = constructor.GetParameters();
          sb.Append("    def __init__(self");
          for (int i = 0; i < parameters.Length; i++)
          {
            if( 0==i )
                sb.Append(", ");
              sb.Append($"{SafePythonName(parameters[i].Name)} : {ToPythonType(parameters[i].ParameterType)}");
            if (i < (parameters.Length - 1))
              sb.Append(", ");
          }
          sb.AppendLine("): ...");
        }
        foreach (var method in stubType.GetMethods())
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
            sb.Append($"    def {propName} (");
          }
          else
            sb.Append($"    def {method.Name} (");

          bool addComma = false;
          if ( !method.IsStatic )
          {
            sb.Append("self");
            addComma = true;
          }
          for( int i=0; i<parameters.Length; i++ )
          {
            if (parameters[i].IsOut)
              continue;

            if( addComma )
              sb.Append(", ");

            sb.Append($"{SafePythonName(parameters[i].Name)} : {ToPythonType(parameters[i].ParameterType)}");
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
      System.IO.File.WriteAllText(path, sb.ToString());
    }

    static string SafePythonName(string s)
    {
      if (s == "from")
        return "from_";
      return s;
    }

    static string ToPythonType(string s)
    {
      string rc = s;
      if (rc.EndsWith("&"))
        rc = rc.Substring(0, rc.Length - 1);

      if (rc.EndsWith("`1") || rc.EndsWith("`2"))
        rc = rc.Substring(0, rc.Length - 2);

      if( rc.EndsWith("[]") )
      {
        string partial = ToPythonType(rc.Substring(0, rc.Length - 2));
        return $"Set({partial})";
      }

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

    static string ToPythonType(Type t)
    {
      if (t.IsGenericType && t.Name.StartsWith("IEnumerable"))
      {
        string rc = ToPythonType(t.GenericTypeArguments[0]);
        return $"Iterable[{rc}]";
      }
      // TODO: Figure out the right way to get at IEnumerable<T>
      if(  t.FullName != null && t.FullName.StartsWith("System.Collections.Generic.IEnumerable`1[["))
      {
        string enumerableType = t.FullName.Substring("System.Collections.Generic.IEnumerable`1[[".Length);
        enumerableType = enumerableType.Substring(0, enumerableType.IndexOf(','));
        var pieces = enumerableType.Split('.');
        string rc = ToPythonType(pieces[pieces.Length-1]);
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
