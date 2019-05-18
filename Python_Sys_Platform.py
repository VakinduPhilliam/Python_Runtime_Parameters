# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# sys.platform. 
# This string contains a platform identifier that can be used to append platform-specific components to sys.path,
# for instance.
# For Unix systems, except on Linux, this is the lowercased OS name as returned by uname -s with the first part of the
# version as returned by uname -r appended, e.g. 'sunos5' or 'freebsd8', at the time when Python was built. Unless you
# want to test for a specific system version, it is therefore recommended to use the following idiom:
 
if sys.platform.startswith('freebsd'):

    # FreeBSD-specific code here...

elif sys.platform.startswith('linux'):

    # Linux-specific code here...
