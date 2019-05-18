# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# classmethod from_callable(obj, *, follow_wrapped=True). 
# Return a Signature (or its subclass) object for a given callable obj. Pass follow_wrapped=False to get a signature of obj
# without unwrapping its __wrapped__ chain.
# This method simplifies subclassing of Signature:
 
class MySignature(Signature):
    pass

sig = MySignature.from_callable(min)
assert isinstance(sig, MySignature)
