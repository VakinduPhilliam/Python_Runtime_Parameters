# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# Post-init processing.
# The generated __init__() code will call a method named __post_init__(), if __post_init__() is defined on the class.
# It will normally be called as self.__post_init__(). However, if any InitVar fields are defined, they will also be passed
# to __post_init__() in the order they were defined in the class. If no __init__() method is generated, then __post_init__()
# will not automatically be called.
# Among other uses, this allows for initializing field values that depend on one or more other fields.
 
@dataclass
class C:

    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):

        self.c = self.a + self.b
