# Python sys � System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib � Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# ExitStack pop_all() 
# Transfers the callback stack to a fresh ExitStack instance and returns it. No callbacks are invoked by this operation - instead, 
# they will now be invoked when the new stack is closed (either explicitly or implicitly at the end of a with statement).
# For example, a group of files can be opened as an �all or nothing� operation as follows:
 
with ExitStack() as stack:
    files = [stack.enter_context(open(fname)) for fname in filenames]

    # Hold onto the close method, but don't call it yet.

    close_files = stack.pop_all().close

    # If opening any file fails, all previously opened files will be
    # closed automatically. If all files are opened successfully,
    # they will remain open even after the with statement ends.
    # close_files() can then be invoked explicitly to close them all.
