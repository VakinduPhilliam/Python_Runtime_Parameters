# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Supporting a variable number of context managers.
# The primary use case for ExitStack is the one given in the class documentation: supporting a variable number of context
# managers and other cleanup operations in a single with statement. The variability may come from the number of context
# managers needed being driven by user input (such as opening a user specified collection of files), or from some of the
# context managers being optional:
 
with ExitStack() as stack:

    for resource in resources:
        stack.enter_context(resource)

    if need_special_resource():
        special = acquire_special_resource()
        stack.callback(release_special_resource, special)

    # Perform operations that use the acquired resources
