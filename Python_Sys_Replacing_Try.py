# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Replacing any use of try-finally and flag variables.
# A pattern you will sometimes see is a try-finally statement with a flag variable to indicate whether or not the body
# of the finally clause should be executed. In its simplest form (that can’t already be handled just by using an except
# clause instead), it looks something like this:
 
cleanup_needed = True

try:
    result = perform_operation()

    if result:
        cleanup_needed = False

finally:

    if cleanup_needed:
        cleanup_resources()
