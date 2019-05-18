# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# contextlib.closing(thing). 
# Return a context manager that closes thing upon completion of the block. This is basically equivalent to:
 
from contextlib import contextmanager

@contextmanager
def closing(thing):

    try:
        yield thing

    finally:
        thing.close()
 
# And lets you write code like this:

# without needing to explicitly close page. Even if an error occurs, page.close() will be called when the with block is
# exited.
  
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:

    for line in page:

        print(line)
 