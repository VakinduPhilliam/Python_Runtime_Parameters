# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# @contextlib.contextmanager. 
# This function is a decorator that can be used to define a factory function for with statement context managers, without
# needing to create a class or separate __enter__() and __exit__() methods.
# While many objects natively support use in with statements, sometimes a resource needs to be managed that isn’t a context
# manager in its own right, and doesn’t implement a close() method for use with contextlib.closing

from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwds):

    # Code to acquire resource, e.g.:

    resource = acquire_resource(*args, **kwds)

    try:
        yield resource

    finally:

        # Code to release resource, e.g.:

        release_resource(resource)

   with managed_resource(timeout=3600) as resource:

        # Resource is released at the end of this block,
        # even if code in the block raises an exception
