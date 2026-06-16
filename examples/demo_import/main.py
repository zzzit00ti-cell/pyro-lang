import sys
import os

# Add the local pyro package to the python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importing pyro automatically registers the import hook for `.pyro` extensions!
import pyro

# Now we can transparently import `.pyro` files as if they were `.py` modules.
import my_module

if __name__ == "__main__":
    print("--- Running Pyro Demo ---")
    my_module.say_hello()
    result = my_module.compute(16)
    print("Computation Result from Pyro:", result)
