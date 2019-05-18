# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Catching exceptions from __enter__ methods.
# It is occasionally desirable to catch exceptions from an __enter__ method implementation, without inadvertently catching
# exceptions from the with statement body or the context manager’s __exit__ method. By using ExitStack the steps in the
# context management protocol can be separated slightly in order to allow this:
 
stack = ExitStack()

try:
    x = stack.enter_context(cm)

except Exception:

    # handle __enter__ exception

else:
    with stack:

        # Handle normal case
