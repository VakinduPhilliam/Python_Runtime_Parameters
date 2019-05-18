# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Reentrant context managers.
# More sophisticated context managers may be “reentrant”. These context managers can not only be used in multiple with
# statements, but may also be used inside a with statement that is already using the same context manager.
# threading.RLock is an example of a reentrant context manager, as are suppress() and redirect_stdout().

from contextlib import redirect_stdout
from io import StringIO

    stream = StringIO()
    write_to_stream = redirect_stdout(stream)

    with write_to_stream:
        print("This is written to the stream rather than stdout")

        with write_to_stream:
            print("This is also written to the stream")

    print("This is written directly to stdout")

       # Displays
       # This is written directly to stdout

    print(stream.getvalue())

       # Displays
       # This is written to the stream rather than stdout
       # This is also written to the stream
