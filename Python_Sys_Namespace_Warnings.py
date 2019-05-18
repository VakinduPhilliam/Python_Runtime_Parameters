# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# warnings — Warning control.
# Warning messages are typically issued in situations where it is useful to alert the user of some condition in a program,
# where that condition (normally) doesn’t warrant raising an exception and terminating the program.
# Developers of interactive shells that run user code in a namespace other than __main__ are advised to ensure that DeprecationWarning
# messages are made visible by default, using code like the following (where user_ns is the module used to execute code entered
# interactively):
 
import warnings

warnings.filterwarnings("default", category=DeprecationWarning,
                                   module=user_ns.get("__name__"))
