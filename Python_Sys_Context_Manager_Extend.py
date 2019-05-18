# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Existing context managers that already have a base class can be extended by using ContextDecorator as a mixin class:
 
from contextlib import ContextDecorator

class mycontext(ContextBaseClass, ContextDecorator):

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False
