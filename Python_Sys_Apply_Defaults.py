# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# apply_defaults()
# Set default values for missing arguments.
# For variable-positional arguments (*args) the default is an empty tuple.
# For variable-keyword arguments (**kwargs) the default is an empty dict.
 
def foo(a, b='ham', *args): pass
    ba = inspect.signature(foo).bind('spam')
    ba.apply_defaults()
    ba.arguments

# OrderedDict([('a', 'spam'), ('b', 'ham'), ('args', ())])

# The args and kwargs properties can be used to invoke functions:
 

def test(a, *, b):

sig = signature(test)

ba = sig.bind(10, b=20)

test(*ba.args, **ba.kwargs)
