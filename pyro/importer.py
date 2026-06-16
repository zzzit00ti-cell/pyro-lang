import sys
import os
import importlib.abc
import importlib.util
from .compiler import compile_pyro

class PyroLoader(importlib.abc.Loader):
    def __init__(self, filename):
        self.filename = filename

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        with open(self.filename, 'r', encoding='utf-8') as f:
            source = f.read()
        
        # Compile pyro syntax into standard python code string
        compiled_code = compile_pyro(source)
        
        # Compile to python code object
        code_obj = compile(compiled_code, self.filename, 'exec')
        
        # Execute the code object in the module's namespace
        exec(code_obj, module.__dict__)

class PyroMetaFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if path is None:
            path = sys.path
            
        name = fullname.split('.')[-1]
        
        for d in path:
            pyro_path = os.path.join(d, name + '.pyro')
            if os.path.exists(pyro_path):
                return importlib.util.spec_from_loader(
                    fullname, PyroLoader(pyro_path), origin=pyro_path
                )
        return None

def register_hook():
    """Register the import hook so `.pyro` files can be imported directly."""
    if not any(isinstance(f, PyroMetaFinder) for f in sys.meta_path):
        sys.meta_path.append(PyroMetaFinder())
