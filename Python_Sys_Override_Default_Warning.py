# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# warnings — Warning control.
# Warning messages are typically issued in situations where it is useful to alert the user of some condition in a program,
# where that condition (normally) doesn’t warrant raising an exception and terminating the program.
# Overriding the default filter.
# Developers of applications written in Python may wish to hide all Python level warnings from their users by default, and
# only display them when running tests or otherwise working on the application.
# The sys.warnoptions attribute used to pass filter configurations to the interpreter can be used as a marker to indicate
# whether or not warnings should be disabled:
 
import sys

if not sys.warnoptions:

    import warnings

    warnings.simplefilter("ignore")
