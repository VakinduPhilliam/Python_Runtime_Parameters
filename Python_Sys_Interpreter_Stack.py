# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# The interpreter stack.
# When the following functions return “frame records,” each record is a named tuple FrameInfo(frame, filename, lineno, function,
# code_context, index). The tuple contains the frame object, the filename, the line number of the current line, the function name,
# a list of lines of context from the source code, and the index of the current line within that list.

def handle_stackframe_without_leak():

    frame = inspect.currentframe()

    try:

        # do something with the frame

    finally:
        del frame
