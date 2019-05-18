# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# builtins — Built-in objects
# This module provides direct access to all ‘built-in’ identifiers of Python; for example, builtins.open is the full
# name for the built-in function open(). 

import builtins

def open(path):

    f = builtins.open(path, 'r')

    return UpperCaser(f)

class UpperCaser:
    '''Wrapper around a file that converts output to upper-case.'''

    def __init__(self, f):
        self._f = f

    def read(self, count=-1):

        return self._f.read(count).upper()

    # ...
