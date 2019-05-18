# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# Basic Example

@dataclass
class C:

    a: int       # 'a' has no default value
    b: int = 0   # assign a default value for 'b'
