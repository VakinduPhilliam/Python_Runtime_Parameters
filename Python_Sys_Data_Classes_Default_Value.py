# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# If the default value of a field is specified by a call to field(), then the class attribute for this field will be replaced
# by the specified default value. If no default is provided, then the class attribute will be deleted. The intent is that after
# the dataclass() decorator runs, the class attributes will all contain the default values for the fields, just as if the default
# value itself were specified. For example, after:
 
@dataclass
class C:

    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    t: int = 20
