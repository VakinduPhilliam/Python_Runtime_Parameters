# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Single use, reusable and reentrant context managers.
# Most context managers are written in a way that means they can only be used effectively in a with statement once.
# These single use context managers must be created afresh each time they’re used - attempting to use them a second time
# will trigger an exception or otherwise not work correctly.
# Context managers created using contextmanager() are also single use context managers, and will complain about the
# underlying generator failing to yield if an attempt is made to use them a second time:
 
from contextlib import contextmanager
    @contextmanager
    def singleuse():
        print("Before")
        yield
        print("After")

    cm = singleuse()

    with cm:
        pass

# Displays

# Before
# After

    with cm:
        pass

# Displays   
# Traceback (most recent call last):
# RuntimeError: generator didn't yield
