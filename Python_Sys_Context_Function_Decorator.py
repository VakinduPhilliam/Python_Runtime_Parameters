# Python sys � System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# contextlib � Utilities for with-statement contexts.
# This module provides utilities for common tasks involving the with statement. 
# Using a context manager as a function decorator.
# ContextDecorator makes it possible to use a context manager in both an ordinary with statement and also as a function
# decorator.
# For example, it is sometimes useful to wrap functions or groups of statements with a logger that can track the time of
# entry and time of exit. Rather than writing both a function decorator and a context manager for the task, inheriting
# from ContextDecorator provides both capabilities in a single definition:
 
from contextlib import ContextDecorator
import logging

logging.basicConfig(level=logging.INFO)

class track_entry_and_exit(ContextDecorator):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        logging.info('Entering: %s', self.name)

    def __exit__(self, exc_type, exc, exc_tb):
        logging.info('Exiting: %s', self.name)
 
# Instances of this class can be used as both a context manager:
 
with track_entry_and_exit('widget loader'):
    print('Some time consuming activity goes here')

    load_widget()
 
# And also as a function decorator:
 
@track_entry_and_exit('widget loader')

def activity():
    print('Some time consuming activity goes here')

    load_widget()
