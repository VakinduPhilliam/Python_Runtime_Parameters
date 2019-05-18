# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# contextlib.nullcontext(enter_result=None). 
# Return a context manager that returns enter_result from __enter__, but otherwise does nothing.
# It is intended to be used as a stand-in for an optional context manager:
 
def myfunction(arg, ignore_exceptions=False):

    if ignore_exceptions:

        # Use suppress to ignore all exceptions.

        cm = contextlib.suppress(Exception)

    else:

        # Do not ignore any exceptions, cm has no effect.

        cm = contextlib.nullcontext()

    with cm:

        # Do something
 
# An example using enter_result:
 
def process_file(file_or_path):

    if isinstance(file_or_path, str):

        # If string, open file

        cm = open(file_or_path)

    else:

        # Caller is responsible for closing file

        cm = nullcontext(file_or_path)

    with cm as file:

        # Perform processing on the file
