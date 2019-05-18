# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# dataclasses — Data Classes.
# This module provides a decorator and functions for automatically adding generated special methods such as __init__()
# and __repr__() to user-defined classes. 
# The member variables to use in these generated methods are defined using PEP 526 type annotations. For example this code:
 
@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''

    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:

        return self.unit_price * self.quantity_on_hand

