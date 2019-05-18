# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# warnings — Warning control.
# Warning messages are typically issued in situations where it is useful to alert the user of some condition in a program,
# where that condition (normally) doesn’t warrant raising an exception and terminating the program.
# Testing Warnings.
# To test warnings raised by code, use the catch_warnings context manager. With it you can temporarily mutate the warnings
# filter to facilitate your testing. For instance, do the following to capture all raised warnings to check:
 
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings(record=True) as w:

    # Cause all warnings to always be triggered.

    warnings.simplefilter("always")

    # Trigger a warning.

    fxn()

    # Verify some things

    assert len(w) == 1
    assert issubclass(w[-1].category, DeprecationWarning)

    assert "deprecated" in str(w[-1].message)
