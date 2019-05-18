# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# inspect.isasyncgenfunction(object). 
# Return true if the object is an asynchronous generator function.
 
async def agen():
        yield 1

inspect.isasyncgenfunction(agen)         # Displays 'True'
