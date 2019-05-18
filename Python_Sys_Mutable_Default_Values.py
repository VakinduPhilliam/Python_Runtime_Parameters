# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 

# Mutable default values.
# Python stores default member variable values in class attributes.
 

class C:
    x = []

    def add(self, element):
        self.x.append(element)

o1 = C()
o2 = C()

o1.add(1)
o2.add(2)

assert o1.x == [1, 2]
assert o1.x is o2.x
 
# Note that the two instances of class C share the same class variable x, as expected. 
# Using dataclasses, if this code was valid:
 

@dataclass
class D:
    x: List = []

    def add(self, element):
        self.x += element
 
# It would generate code similar to:
 

class D:
    x = []

    def __init__(self, x=x):
        self.x = x

    def add(self, element):
        self.x += element

assert D().x is D().x
 
# This has the same issue as the original example using class C. That is, two instances of class D that do not specify a
# value for x when creating a class instance will share the same copy of x. Because dataclasses just use normal Python class
# creation they also share this behavior. There is no general way for Data Classes to detect this condition. Instead, dataclasses
# will raise a TypeError if it detects a default parameter of type list, dict, or set. This is a partial solution, but it does
# protect against many common errors.
# Using default factory functions is a way to create new instances of mutable types as default values for fields:
 

@dataclass
class D:

    x: list = field(default_factory=list)

assert D().x is not D().x
