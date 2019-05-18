# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# warnings — Warning control.
# Warning messages are typically issued in situations where it is useful to alert the user of some condition in a program,
# where that condition (normally) doesn’t warrant raising an exception and terminating the program.

# Individual warnings filters are specified as a sequence of fields separated by colons:
 
action:message:category:module:line

# Commonly used warning filters apply to either all warnings, warnings in a particular category, or warnings raised by particular
# modules or packages. Some examples:
 
default                      # Show all warnings (even those ignored by default)
ignore                       # Ignore all warnings
error                        # Convert all warnings to errors
error::ResourceWarning       # Treat ResourceWarning messages as errors
default::DeprecationWarning  # Show DeprecationWarning messages
ignore,default:::mymodule    # Only report warnings triggered by "mymodule"
error:::mymodule[.*]         # Convert warnings to errors in "mymodule"
                             # and any subpackages of "mymodule"

# Default Warning Filter.
# By default, Python installs several warning filters, which can be overridden by the -W command-line option, the PYTHONWARNINGS environment
# variable and calls to filterwarnings().
# In regular release builds, the default warning filter has the following entries (in order of precedence):

default::DeprecationWarning:__main__
ignore::DeprecationWarning
ignore::PendingDeprecationWarning
ignore::ImportWarning
ignore::ResourceWarning
