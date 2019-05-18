# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# Fetching attributes statically.
# inspect.getattr_static(obj, attr, default=None). 
# Retrieve attributes without triggering dynamic lookup via the descriptor protocol, __getattr__() or __getattribute__().
# example code for resolving the builtin descriptor types.

class _foo:
    __slots__ = ['foo']

slot_descriptor = type(_foo.foo)
getset_descriptor = type(type(open(__file__)).name)
wrapper_descriptor = type(str.__dict__['__add__'])

descriptor_types = (slot_descriptor, getset_descriptor, wrapper_descriptor)

result = getattr_static(some_object, 'foo')

if type(result) in descriptor_types:

    try:
        result = result.__get__()

    except AttributeError:

        # descriptors can raise AttributeError to
        # indicate there is no underlying value
        # in which case the descriptor itself will
        # have to do

        pass
