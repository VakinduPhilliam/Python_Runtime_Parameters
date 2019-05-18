# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Reusing a single stack object across multiple with statements works correctly,
# but attempting to nest them will cause the stack to be cleared at the end of the innermost with statement, which is
# unlikely to be desirable behaviour.
# Using separate ExitStack instances instead of reusing a single instance avoids that problem:
 
from contextlib import ExitStack

    with ExitStack() as outer_stack:
        outer_stack.callback(print, "Callback: from outer context")

        with ExitStack() as inner_stack:
            inner_stack.callback(print, "Callback: from inner context")

            print("Leaving inner context")
        print("Leaving outer context")

# Displays
# Leaving inner context
# Callback: from inner context
# Leaving outer context
# Callback: from outer context
