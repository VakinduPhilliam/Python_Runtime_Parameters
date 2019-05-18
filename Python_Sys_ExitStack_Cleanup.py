# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# If the resource cleanup isn’t already neatly bundled into a standalone function, then it is still possible to use
# the decorator form of ExitStack.callback() to declare the resource cleanup in advance:
 
from contextlib import ExitStack

with ExitStack() as stack:
    @stack.callback
    def cleanup_resources():

    result = perform_operation()

    if result:
        stack.pop_all()
