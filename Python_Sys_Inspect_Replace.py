# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# replace(*[, parameters][, return_annotation]). 
# Create a new Signature instance based on the instance replace was invoked on. It is possible to pass different parameters
# and/or return_annotation to override the corresponding properties of the base signature. To remove return_annotation from
# the copied Signature, pass in Signature.empty.

def test(a, b):
        pass

    sig = signature(test)
    new_sig = sig.replace(return_annotation="new return anno")

    str(new_sig)       # Displays "(a, b) -> 'new return anno'"
