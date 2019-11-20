"""Import statements tell python what packages you'll be using.

You can use 'as' to change how you refer to the package. In this file,
I import matplotlib.pyplot as plt so I don't have to type out
'matplotlib.pyplot' every time I want to use it.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###############################################################################
"""After the import statements, I define function(s).
Function definitions start with the word 'def' and end when
the indentation ends. For example:


def ex1():
    print("This line is part of the function 'ex1' because it's indented")
    print("This line is still part of the function 'ex1'")
    print("Blank lines do not end the current level of indentation")

print("This line is not part of the function 'ex1' because it's not indented")


"""


###############################################################################
# These next lines 'call' the functions defined above.
# If you erase the lines below (or put a # in front of them) this code won't
# 'do' anything (it won't generate a graph anymore.)
