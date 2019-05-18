# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# Init-only variables.
# The other place where dataclass() inspects a type annotation is to determine if a field is an init-only variable.
# It does this by seeing if the type of a field is of type dataclasses.InitVar. If a field is an InitVar, it is considered
# a pseudo-field called an init-only field.

@dataclass
class C:

    i: int
    j: int = None

    database: InitVar[DatabaseType] = None

    def __post_init__(self, database):

        if self.j is None and database is not None:

            self.j = database.lookup('j')

c = C(10, database=my_database)
