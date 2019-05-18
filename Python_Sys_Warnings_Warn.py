# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# warnings — Warning control.
# Warning messages are typically issued in situations where it is useful to alert the user of some condition in a program,
# where that condition (normally) doesn’t warrant raising an exception and terminating the program.
# Available Functions.
# warnings.warn(message, category=None, stacklevel=1, source=None). 
# Issue a warning, or maybe ignore it or raise an exception. The category argument, if given, must be a warning category class;
# it defaults to UserWarning. 

def deprecation(message):

    warnings.warn(message, DeprecationWarning, stacklevel=2)
