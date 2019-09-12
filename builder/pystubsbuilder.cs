using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;
using System.IO;

using DocoptNet;
using PythonStubs;

namespace pystubsbuilder {
    class Program {
        private const string UsagePatterns = @"
Usage:
    pystubsbuilder (-h | --help)
    pystubsbuilder (-V | --version)
    pystubsbuilder [--dest=<dest_path>] [--search=<search_path>...] <target_dll>...

Options:
    -h --help                   Show this help
    -V --version                Show version
    --dest=<dest_path>          Path to save the subs to
    --search=<search_path>      Path to search for referenced assemblies
";

        static void Main(string[] args) {
            var arguments = new Docopt().Apply(UsagePatterns, args, version: Assembly.GetExecutingAssembly().GetName().Version, exit: true);

            if (arguments.ContainsKey("<target_dll>"))
                foreach (ValueObject targetDll in (ArrayList)arguments["<target_dll>"].Value) {
                    string assmPath = (string)targetDll.Value;
                    if (File.Exists(assmPath)) {
                        // grab dest path if provided
                        string destPath = null;
                        if (arguments["--dest"] != null && arguments["--dest"].IsString)
                            destPath = (string)arguments["--dest"].Value;
                        Console.WriteLine($"target path is {destPath}");

                        // grab searchp paths if provided
                        string[] searchPaths = null;
                        if (arguments["--search"] != null && arguments["--search"].IsList) {
                            List<string> lookupPaths = new List<string>();
                            foreach (ValueObject searchPath in arguments["--search"].AsList.ToArray()) {
                                Console.WriteLine($"search path {searchPath}");
                                lookupPaths.Add((string)searchPath.Value);
                            }
                            searchPaths = lookupPaths.ToArray();
                        }

                        Console.WriteLine($"building stubs for {assmPath}");
                        try {
                            var dest = PythonStubsBuilder.BuildAssemblyStubs(assmPath, destPath: destPath, searchPaths: searchPaths);
                            Console.WriteLine($"stubs saved to {dest}");
                        }
                        catch (Exception sgEx) {
                            Console.WriteLine($"error: failed generating stubs | {sgEx.Message}");
                        }
                    }
                    else {
                        Console.WriteLine($"error: can not find {assmPath}");
                    }
                }
        }
    }
}
