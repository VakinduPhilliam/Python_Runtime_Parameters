# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# dataclasses.astuple(instance, *, tuple_factory=tuple). 
# Converts the dataclass instance to a tuple (by using the factory function tuple_factory). Each dataclass is converted
# to a tuple of its field values. dataclasses, dicts, lists, and tuples are recursed into.

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

assert astuple(p) == (10, 20)
assert astuple(c) == ([(0, 0), (10, 4)],)

