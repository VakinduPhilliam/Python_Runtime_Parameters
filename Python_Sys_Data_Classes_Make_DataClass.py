# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# dataclasses.make_dataclass(cls_name, fields, *, bases=(), namespace=None, init=True, repr=True, eq=True, order=False, 
# unsafe_hash=False, frozen=False)
# Creates a new dataclass with name cls_name, fields as defined in fields, base classes as given in bases, and initialized
# with a namespace as given in namespace.
# This function is provided as a convenience.
 
C = make_dataclass('C',
                   [('x', int),
                     'y',
                    ('z', int, field(default=5))],
                   namespace={'add_one': lambda self: self.x + 1})

# 
# Is equivalent to:
# 

@dataclass
class C:

    x: int
    y: 'typing.Any'
    z: int = 5

    def add_one(self):

        return self.x + 1
