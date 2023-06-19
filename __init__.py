from binaryninja import BinaryView
from binaryninja import PluginCommand
from rust_demangler import demangle
from rust_demangler.rust import TypeNotFoundError
from rust_demangler.rust_legacy import UnableToLegacyDemangle
from rust_demangler.rust_v0 import UnableTov0Demangle

def demangle_functions(bv: BinaryView):
    bv.begin_undo_actions()
    for f in bv.functions:
        try:
            f.name = demangle(f.symbol.raw_name)
        # Not a valid mangled name
        except TypeNotFoundError:
            pass
        except UnableToLegacyDemangle:
            pass
        except UnableTov0Demangle:
            pass
    bv.commit_undo_actions()

PluginCommand.register("Rust Demangle", "Demangles Rust symbols.", demangle_functions)
