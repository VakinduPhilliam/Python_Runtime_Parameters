# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib — Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# @contextlib.asynccontextmanager 
# Similar to contextmanager(), but creates an asynchronous context manager.
# This function is a decorator that can be used to define a factory function for async with statement asynchronous context
# managers, without needing to create a class or separate __aenter__() and __aexit__() methods.
# It must be applied to an asynchronous generator function.
# A simple example:
 
from contextlib import asynccontextmanager

@asynccontextmanager

async def get_connection():

    conn = await acquire_db_connection()

    try:
        yield conn

    finally:
        await release_db_connection(conn)

async def get_all_users():

    async with get_connection() as conn:

        return conn.query('SELECT ...')
