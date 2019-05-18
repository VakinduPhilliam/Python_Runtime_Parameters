# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# Inheritance.
# When the dataclass is being created by the dataclass() decorator, it looks through all of the class’s base classes in
# reverse MRO (that is, starting at object) and, for each dataclass that it finds, adds the fields from that base class
# to an ordered mapping of fields. After all of the base class fields are added, it adds its own fields to the ordered mapping.
# All of the generated methods will use this combined, calculated ordered mapping of fields. Because the fields are in insertion
# order, derived classes override base classes.
 
@dataclass
class Base:

    x: Any = 15.0
    y: int = 0

@dataclass
class C(Base):

    z: int = 10
    x: int = 15

