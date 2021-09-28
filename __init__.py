from binaryninja import PluginCommand
from rust_demangler import demangle
from rust_demangler.rust import TypeNotFoundError

def demangle_functions(bv):
    for f in bv.functions:
        try:
            f.name = demangle(f.symbol.raw_name)
        # Not a valid mangled name
        except TypeNotFoundError:
            pass

PluginCommand.register("Rust Demangle", "Demangles Rust symbols.", demangle_functions)
