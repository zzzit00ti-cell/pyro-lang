import sys
from .compiler import compile_pyro, compile_file
from .cli import main
from .importer import register_hook

# Register the hook so `.pyro` file imports work seamlessly
register_hook()

if sys.version_info < (3, 10):
    raise ImportError("Pyro requires Python 3.10 or higher")
__version__ = "2.0.0"
__all__ = ["compile_pyro", "compile_file", "main"]
