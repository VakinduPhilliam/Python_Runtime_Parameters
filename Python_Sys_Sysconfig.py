# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# sysconfig — Provide access to Python’s configuration information.
# sysconfig.get_config_var(name). 
# Return the value of a single variable name. Equivalent to get_config_vars().get(name).
# If name is not found, return None.
 

import sysconfig

sysconfig.get_config_var('Py_ENABLE_SHARED')

# Displays '0'

sysconfig.get_config_var('LIBDIR')

# Displays '/usr/local/lib'

sysconfig.get_config_vars('AR', 'CXX')

# Displays ['ar', 'g++']
