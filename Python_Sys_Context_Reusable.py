# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Reusable context managers.
# Another example of a reusable, but not reentrant, context manager is ExitStack, as it invokes all currently registered
# callbacks when leaving any with statement, regardless of where those callbacks were added:
 
from contextlib import ExitStack
    stack = ExitStack()

    with stack:
        stack.callback(print, "Callback: from first context")
        print("Leaving first context")

# Displays
# Leaving first context
# Callback: from first context

    with stack:
        stack.callback(print, "Callback: from second context")
        print("Leaving second context")

# Displays
# Leaving second context
# Callback: from second context

    with stack:
        stack.callback(print, "Callback: from outer context")

        with stack:
            stack.callback(print, "Callback: from inner context")
            print("Leaving inner context")

        print("Leaving outer context")

# Displays
# Leaving inner context
# Callback: from inner context
# Callback: from outer context
# Leaving outer context
