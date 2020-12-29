from binaryninja import *
from rust_demangle import demangle

def demangle_functions(bv):
    for f in bv.functions:
        f.name = demangle(f.symbol.raw_name)

PluginCommand.register("Rust Demangle", "Demangles Rust symbols.", demangle_functions)
