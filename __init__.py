from binaryninja import BinaryView
from binaryninja import PluginCommand
from binaryninja import Symbol, SymbolType
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
    for sym in bv.symbols.values():
        for symbol in sym:
            if symbol.type == SymbolType.ExternalSymbol:
                try:
                    user_sym = Symbol(symbol.type, symbol.address, demangle(symbol.raw_name))
                except TypeNotFoundError:
                    pass
                except UnableToLegacyDemangle:
                    pass
                except UnableTov0Demangle:
                    pass
                bv.define_user_symbol(user_sym)

    bv.commit_undo_actions()

PluginCommand.register("Rust Demangle", "Demangles Rust symbols.", demangle_functions)
