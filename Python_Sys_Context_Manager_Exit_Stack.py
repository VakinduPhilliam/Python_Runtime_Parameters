# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# class contextlib.ExitStack. 
# A context manager that is designed to make it easy to programmatically combine other context managers and cleanup
# functions, especially those that are optional or otherwise driven by input data.
# For example, a set of files may easily be handled in a single with statement as follows:
 
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]

    # All opened files will automatically be closed at the end of
    # the with statement, even if attempts to open files later
    # in the list raise an exception
