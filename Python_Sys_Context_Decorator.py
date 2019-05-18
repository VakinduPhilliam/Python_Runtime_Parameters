# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# class contextlib.ContextDecorator. 
# A base class that enables a context manager to also be used as a decorator.
# Context managers inheriting from ContextDecorator have to implement __enter__ and __exit__ as normal. __exit__ retains
# its optional exception handling even when used as a decorator.
# ContextDecorator is used by contextmanager(), so you get this functionality automatically.

from contextlib import ContextDecorator

class mycontext(ContextDecorator):

    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self, *exc):
        print('Finishing')
        return False

    @mycontext()
    def function():
        print('The bit in the middle')

   function()

# Display
# Starting
# The bit in the middle
# Finishing

    with mycontext():
        print('The bit in the middle')

# Display
# Starting
# The bit in the middle
# Finishing
 
#
# This change is just syntactic sugar for any construct of the following form:
# 

def f():
    with cm():

        # Do stuff
 
#
# ContextDecorator lets you instead write:
# 

@cm()
def f():

    # Do stuff
