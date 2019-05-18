# Python sys � System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib � Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# atexit � Exit handlers.
# The atexit module defines functions to register and unregister cleanup functions.
# Functions thus registered are automatically executed upon normal interpreter termination. atexit runs these functions
# in the reverse order in which they were registered; if you register A, B, and C, at interpreter termination time they
# will be run in the order C, B, A.
# The following simple example demonstrates how a module can initialize a counter from a file when it is imported and save
# the counter�s updated value automatically when the program terminates without relying on the application making an explicit
# call into this module at termination.
 
try:
    with open("counterfile") as infile:
        _count = int(infile.read())

except FileNotFoundError:
    _count = 0

def incrcounter(n):
    global _count
    _count = _count + n

def savecounter():
    with open("counterfile", "w") as outfile:
        outfile.write("%d" % _count)

import atexit

atexit.register(savecounter)

# 
# Positional and keyword arguments may also be passed to register() to be passed along to the registered function when it is
# called:
# 

def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

import atexit

atexit.register(goodbye, 'Donny', 'nice')

#
# or:
#

atexit.register(goodbye, adjective='nice', name='Donny')
 
#
# Usage as a decorator:
# 

import atexit

@atexit.register
def goodbye():

    print("You are now leaving the Python sector.")