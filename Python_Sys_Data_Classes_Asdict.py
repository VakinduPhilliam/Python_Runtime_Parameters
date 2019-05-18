# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# dataclasses.asdict(instance, *, dict_factory=dict). 
# Converts the dataclass instance to a dict (by using the factory function dict_factory). Each dataclass is converted
# to a dict of its fields, as name: value pairs. dataclasses, dicts, lists, and tuples are recursed into.
 
@dataclass
class Point:

     x: int
     y: int

@dataclass

class C:

     mylist: List[Point]

p = Point(10, 20)

assert asdict(p) == {'x': 10, 'y': 20}

c = C([Point(0, 0), Point(10, 4)])

assert asdict(c) == {'mylist': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}
