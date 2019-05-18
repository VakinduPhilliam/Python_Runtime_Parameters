# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# ExitStack makes it possible to register a callback for execution at the end of a with statement, and then later
# decide to skip executing that callback:
 
from contextlib import ExitStack

with ExitStack() as stack:
    stack.callback(cleanup_resources)

    result = perform_operation()

    if result:
        stack.pop_all()
