# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# dataclasses.field(*, default=MISSING, default_factory=MISSING, repr=True, hash=None, init=True, compare=True, metadata=None)
# For common and simple use cases, no other functionality is required. 
# There are, however, some dataclass features that require additional per-field information. To satisfy this need for additional
# information, you can replace the default field value with a call to the provided field() function. For example:
 
@dataclass
class C:

    mylist: List[int] = field(default_factory=list)

c = C()

c.mylist += [1, 2, 3]
