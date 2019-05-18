# Python sys � System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib � Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Cleaning up in an __enter__ implementation.
# As noted in the documentation of ExitStack.push(), this method can be useful in cleaning up an already allocated resource
# if later steps in the __enter__() implementation fail.
# Here�s an example of doing this for a context manager that accepts resource acquisition and release functions, along with
# an optional validation function, and maps them to the context management protocol:
 
from contextlib import contextmanager, AbstractContextManager, ExitStack

class ResourceManager(AbstractContextManager):

    def __init__(self, acquire_resource, release_resource, check_resource_ok=None):
        self.acquire_resource = acquire_resource
        self.release_resource = release_resource

        if check_resource_ok is None:
            def check_resource_ok(resource):
                return True

        self.check_resource_ok = check_resource_ok

    @contextmanager
    def _cleanup_on_error(self):

        with ExitStack() as stack:
            stack.push(self)
            yield

            # The validation check passed and didn't raise an exception
            # Accordingly, we want to keep the resource, and pass it
            # back to our caller

            stack.pop_all()

    def __enter__(self):
        resource = self.acquire_resource()

        with self._cleanup_on_error():

            if not self.check_resource_ok(resource):
                msg = "Failed validation for {!r}"
                raise RuntimeError(msg.format(resource))

        return resource

    def __exit__(self, *exc_details):

        # We don't need to duplicate any of our resource release logic

        self.release_resource()
