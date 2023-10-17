import sys
from os import system

path = "/F/workspace/TahsinAyman/cli/create-cpp-module/module/**"
module_name = sys.argv[1]
system(f"mkdir {module_name}")
system(f"cp -r {path} {module_name}")