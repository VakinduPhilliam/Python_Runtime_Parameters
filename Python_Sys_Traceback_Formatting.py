# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# traceback — Print or retrieve a stack traceback.
# This module provides a standard interface to extract, format and print stack traces of Python programs.
# It exactly mimics the behavior of the Python interpreter when it prints a stack trace.
# This is useful when you want to print stack traces under program control, such as in a “wrapper” around the interpreter.
# The module uses traceback objects — this is the object type that is stored in the sys.last_traceback variable and returned
# as the third item from sys.exc_info().
# This last example demonstrates the final few formatting functions:
 
import traceback
    traceback.format_list([('spam.py', 3, '<module>', 'spam.eggs()'),
                           ('eggs.py', 42, 'eggs', 'return "bacon"')])

    an_error = IndexError('tuple index out of range')
    traceback.format_exception_only(type(an_error), an_error)
