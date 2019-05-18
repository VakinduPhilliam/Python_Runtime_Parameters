# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# inspect.isawaitable(object). 
# Return true if the object can be used in await expression.
 
# Can also be used to distinguish generator-based coroutines from regular generators:
 

def gen():
    yield

@types.coroutine
def gen_coro():
    yield

assert not isawaitable(gen())
assert isawaitable(gen_coro())
