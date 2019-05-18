# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# inspect.signature(callable, *, follow_wrapped=True). 
# Return a Signature object for the given callable:
 
from inspect import signature

    def foo(a, *, b:int, **kwargs):
        pass

    sig = signature(foo)

    str(sig)           # Displays '(a, *, b:int, **kwargs)'

    str(sig.parameters['b'])   # Displays 'b:int'

    sig.parameters['b'].annotation     # Displays <class 'int'>
