# Python sys — System-specific parameters and functions.
# This module provides access to some variables used or maintained by the interpreter and to functions that interact
# strongly with the interpreter.
# sys.float_info. 
# It's a struct sequence holding information about the float type.
# It contains low level information about the precision and internal representation. 

import sys

sys.float_info.dig            # Displays 15

    s = '3.14159265358979'    # decimal string with 15 significant digits

    format(float(s), '.15g')  # convert to float and back -> same value
                              # Displays  '3.14159265358979'
