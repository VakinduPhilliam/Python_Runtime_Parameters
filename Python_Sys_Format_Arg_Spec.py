# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# inspect — Inspect live objects.
# The inspect module provides several useful functions to help get information about live objects such as modules, classes,
# methods, functions, tracebacks, frame objects, and code objects. 
# inspect.formatargspec(args[, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations[, formatarg, formatvarargs,
# formatvarkw, formatvalue, formatreturns, formatannotations]])
# Format a pretty argument spec from the values returned by getfullargspec().
# The first seven arguments are (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations).
# The other six arguments are functions that are called to turn argument names, * argument name, ** argument name, default
# values, return annotation and individual annotations into strings, respectively.
 
from inspect import formatargspec, getfullargspec
    def f(a: int, b: float):
        pass

    formatargspec(*getfullargspec(f))  # Displays '(a: int, b: float)'
