# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# dataclasses.is_dataclass(class_or_instance). 
# Returns True if its parameter is a dataclass or an instance of one, otherwise returns False.
# If you need to know if a class is an instance of a dataclass (and not a dataclass itself), then add a further check for
# not isinstance(obj, type):
 
def is_dataclass_instance(obj):

    return is_dataclass(obj) and not isinstance(obj, type)
