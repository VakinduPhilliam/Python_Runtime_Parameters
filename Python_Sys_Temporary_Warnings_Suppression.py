# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# warnings — Warning control.
# Warning messages are typically issued in situations where it is useful to alert the user of some condition in a program,
# where that condition (normally) doesn’t warrant raising an exception and terminating the program.
# Temporarily Suppressing Warnings.
# If you are using code that you know will raise a warning, such as a deprecated function, but do not want to see the warning
# (even when warnings have been explicitly configured via the command line), then it is possible to suppress the warning using
# the catch_warnings context manager:
 
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():

    warnings.simplefilter("ignore")

    fxn()

