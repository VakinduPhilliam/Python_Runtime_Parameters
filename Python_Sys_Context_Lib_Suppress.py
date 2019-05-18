# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# contextlib.suppress(*exceptions). 
# Return a context manager that suppresses any of the specified exceptions if they occur in the body of a with statement
# and then resumes execution with the first statement following the end of the with statement.
# As with any other mechanism that completely suppresses exceptions, this context manager should be used only to cover very
# specific errors where silently continuing with program execution is known to be the right thing to do.

from contextlib import suppress

with suppress(FileNotFoundError):

    os.remove('somefile.tmp')

with suppress(FileNotFoundError):

    os.remove('someotherfile.tmp')
 
# This code is equivalent to:

try:
    os.remove('somefile.tmp')

except FileNotFoundError:
    pass

try:
    os.remove('someotherfile.tmp')

except FileNotFoundError:
    pass
