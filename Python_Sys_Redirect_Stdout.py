# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# contextlib.redirect_stdout(new_target). 
# Context manager for temporarily redirecting sys.stdout to another file or file-like object.
 
# This tool adds flexibility to existing functions or classes whose output is hardwired to stdout.
 
# For example, the output of help() normally is sent to sys.stdout. You can capture that output in a string by redirecting
# the output to an io.StringIO object:
 

f = io.StringIO()

with redirect_stdout(f):
    help(pow)

s = f.getvalue()
 
#
# To send the output of help() to a file on disk, redirect the output to a regular file:
# 

with open('help.txt', 'w') as f:

    with redirect_stdout(f):
        help(pow)

# 
# To send the output of help() to sys.stderr:
# 

with redirect_stdout(sys.stderr):
    help(pow)
