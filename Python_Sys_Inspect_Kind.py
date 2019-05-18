# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# print all keyword-only arguments without default values:
 
def foo(a, b, *, c, d=10):
        pass

    sig = signature(foo)

    for param in sig.parameters.values():
        if (param.kind == param.KEYWORD_ONLY and
                           param.default is param.empty):

            print('Parameter:', param)        # Displays 'Parameter: c'
