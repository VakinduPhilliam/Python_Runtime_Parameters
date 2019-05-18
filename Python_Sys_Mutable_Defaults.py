# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# Mutable default values.
# Python stores default member variable values in class attributes. Consider this example, not using dataclasses:
 
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

