# Python sys � System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# sys.displayhook(value). 
# If value is not None, this function prints repr(value) to sys.stdout, and saves value in builtins._. If repr(value)
# is not encodable to sys.stdout.encoding with sys.stdout.errors error handler (which is probably 'strict'), encode it
# to sys.stdout.encoding with 'backslashreplace' error handler.
# sys.displayhook is called on the result of evaluating an expression entered in an interactive Python session.
# The display of these values can be customized by assigning another one-argument function to sys.displayhook.

# The Pseudo-code:
 
def displayhook(value):

    if value is None:
        return

    # Set '_' to None to avoid recursion

    builtins._ = None
    text = repr(value)

    try:
        sys.stdout.write(text)

    except UnicodeEncodeError:
        bytes = text.encode(sys.stdout.encoding, 'backslashreplace')

        if hasattr(sys.stdout, 'buffer'):
            sys.stdout.buffer.write(bytes)

        else:
            text = bytes.decode(sys.stdout.encoding, 'strict')
            sys.stdout.write(text)

    sys.stdout.write("\n")

    builtins._ = value
