# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# sys.set_coroutine_wrapper(wrapper). 
# Allows intercepting creation of coroutine objects (only ones that are created by an async def function; generators
# decorated with types.coroutine() or asyncio.coroutine() will not be intercepted).
# The wrapper argument must be either:
# > a callable that accepts one argument (a coroutine object);
# > 'None', to reset the wrapper.
# If called twice, the new wrapper replaces the previous one. The function is thread-specific.
# The wrapper callable cannot define new coroutines directly or indirectly:
 
def wrapper(coro):

    async def wrap(coro):
        return await coro

    return wrap(coro)

sys.set_coroutine_wrapper(wrapper)

async def foo():
    pass

# The following line will fail with a RuntimeError, because
# ``wrapper`` creates a ``wrap(coro)`` coroutine:

foo()


