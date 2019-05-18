# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# sys.hexversion. 
# The version number encoded as a single integer. This is guaranteed to increase with each version, including proper
# support for non-production releases. For example, to test that the Python interpreter is at least version 1.5.2, use:
 
if sys.hexversion >= 0x010502F0:
    # use some advanced feature
    ...

else:
    # use an alternative implementation or warn the user
    ...


