# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# abc — Abstract Base Classes
# This module provides the infrastructure for defining abstract base classes (ABCs)

# class abc.ABC 
# A helper class that has ABCMeta as its metaclass. With this class, an abstract base class can be created by simply
# deriving from ABC avoiding sometimes confusing metaclass usage, for example:
 
from abc import ABC

class MyABC(ABC):
    pass
 
# Note that the type of ABC is still ABCMeta, therefore inheriting from ABC requires the usual precautions regarding metaclass
# usage, as multiple inheritance may lead to metaclass conflicts. One may also define an abstract base class by passing the
# metaclass keyword and using ABCMeta directly, for example:
 
from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    pass
 

# class abc.ABCMeta 
# Metaclass for defining Abstract Base Classes (ABCs).
# Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. 
# You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as “virtual subclasses” – these
# and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the
# registering ABC won’t show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC
# be callable (not even via super()).
 
from abc import ABC

class MyABC(ABC):
    pass

MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)
 

# You can also override this method in an abstract base class:
#  __subclasshook__(subclass) 
# (Must be defined as a class method.)

class Foo:
    def __getitem__(self, index):

    def __len__(self):

    def get_iterator(self):
        return iter(self)

class MyIterable(ABC):

    @abstractmethod

    def __iter__(self):

        while False:
            yield None

    def get_iterator(self):

        return self.__iter__()

    @classmethod
    def __subclasshook__(cls, C):

        if cls is MyIterable:

            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

MyIterable.register(Foo)
 
# The abc module also provides the following decorator:
# @abc.abstractmethod 
# A decorator indicating abstract methods.
# Using this decorator requires that the class’s metaclass is ABCMeta or is derived from it. 

class C(ABC):

    @abstractmethod
    def my_abstract_method(self, ...):


    @classmethod
    @abstractmethod
    def my_abstract_classmethod(cls, ...):

    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod(...):
        ...

    @property
    @abstractmethod
    def my_abstract_property(self):

    @my_abstract_property.setter
    @abstractmethod
    def my_abstract_property(self, val):

    @abstractmethod
    def _get_x(self):

    @abstractmethod
    def _set_x(self, val):

    x = property(_get_x, _set_x)
 
# In order to correctly interoperate with the abstract base class machinery, the descriptor must identify itself as abstract
# using __isabstractmethod__. In general, this attribute should be True if any of the methods used to compose the descriptor
# are abstract.

class Descriptor:

    @property
    def __isabstractmethod__(self):

        return any(getattr(f, '__isabstractmethod__', False) for

                   f in (self._fget, self._fset, self._fdel))
 
# @abc.abstractclassmethod 
# It is now possible to use classmethod with abstractmethod(), making this decorator redundant.
# A subclass of the built-in classmethod(), indicating an abstract classmethod. Otherwise it is similar to abstractmethod().
# This special case is deprecated, as the classmethod() decorator is now correctly identified as abstract when applied to
# an abstract method:
 
class C(ABC):
    @classmethod
    @abstractmethod

    def my_abstract_classmethod(cls, ...):

 @abc.abstractstaticmethod 

# It is now possible to use staticmethod with abstractmethod(), making this decorator redundant.
# A subclass of the built-in staticmethod(), indicating an abstract staticmethod. Otherwise it is similar to abstractmethod().
# This special case is deprecated, as the staticmethod() decorator is now correctly identified as abstract when applied to an
# abstract method:
 
class C(ABC):
    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod(...):

 @abc.abstractproperty 

# It is now possible to use property, property.getter(), property.setter() and property.deleter() with abstractmethod(), making
# this decorator redundant.
# A subclass of the built-in property(), indicating an abstract property.
# This special case is deprecated, as the property() decorator is now correctly identified as abstract when applied to an abstract method:
 
class C(ABC):
    @property
    @abstractmethod
    def my_abstract_property(self):
 
# The above example defines a read-only property; you can also define a read-write abstract property by appropriately marking one
# or more of the underlying methods as abstract:
 

class C(ABC):
    @property
    def x(self):

    @x.setter
    @abstractmethod
    def x(self, val):
 
# If only some components are abstract, only those components need to be updated to create a concrete property in a subclass:
 
class D(C):
    @C.x.setter
    def x(self, val):
