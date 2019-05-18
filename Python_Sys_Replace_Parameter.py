# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# replace(*[, name][, kind][, default][, annotation]). 
# Create a new Parameter instance based on the instance replaced was invoked on. To override a Parameter attribute, pass the
# corresponding argument. To remove a default value or/and an annotation from a Parameter, pass Parameter.empty.
 
from inspect import Parameter

    param = Parameter('foo', Parameter.KEYWORD_ONLY, default=42)

    str(param)              # Displays 'foo=42'

    str(param.replace())    # Will create a shallow copy of 'param'

                            # Displays'foo=42'

    str(param.replace(default=Parameter.empty, annotation='spam'))

                            # Displays "foo:'spam'"
