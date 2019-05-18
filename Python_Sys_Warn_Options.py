# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# warnings — Warning control.
# Warning messages are typically issued in situations where it is useful to alert the user of some condition in a program,
# where that condition (normally) doesn’t warrant raising an exception and terminating the program.
# Developers of test runners for Python code are advised to ensure that all warnings are displayed by default for the
# code under test, using code like:
 
import sys

if not sys.warnoptions:

    import os, warnings

    warnings.simplefilter("default")           # Change the filter in this process

    os.environ["PYTHONWARNINGS"] = "default"   # Also affect subprocesses
