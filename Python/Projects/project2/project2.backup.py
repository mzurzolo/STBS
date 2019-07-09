import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###############################################################################

def plot_without_pandas():
    """Generate plot, without pandas."""
    # This method does not rely on the read_csv() function
    # that pandas provides.

    # This will make an empty 'list' for each column in data.csv
    # See https://docs.python.org/3/tutorial/introduction.html#lists
    # for more on lists.
    x = []
    y = []
    sin = []
    cos = []

    # See https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
    # for more on reading and writing files.
    with open("inputs/data.csv", "r") as file:
        # I know that the first line contains column names, not
        # actual data. By calling file.readline() on the file, I skip
        # past the column names
        column_names = file.readline()
        # Notice how the indentation level increased (an it increases again below)
        # In python, lines of code are grouped by indentation level.
        print(column_names)
        # this will loop through each line in the file.
        # each indented line of code will run once for every line of data in data.csv

        for line in file:
            # Split each line into a list of values,
            # using a comma as the separation point
            split_line = line.split(",")
            # These next lines store the values in split_line to temporary
            # variables. Counting typically starts at 0 for most programming
            # languages.
            x_temp = split_line[0]  # This line means:
                                    # "take the first value in split_line, and call it x_temp"
            y_temp = split_line[1]
            sin_temp = split_line[2]
            cos_temp = split_line[3]

            # These next lines make sure our temporary variables are being
            # stored as numbers. 'float' is short for 'floating-point decimal'
            # Think of these lines as saying:
            #   "Our temporary variables hold numbers that may have a decimal"
            x_temp = float(x_temp)
            y_temp = float(y_temp)
            sin_temp = float(sin_temp)
            cos_temp = float(cos_temp)

            # These next lines will add our temporary variables to the end of
            # our lists (we created them above.)
            # Every time this loop runs, our lists will grow by 1 element.
            x.append(x_temp)
            y.append(y_temp)
            sin.append(sin_temp)
            cos.append(cos_temp)

            # If you want to watch the list grow, you can use python's input
            # function. Input will print a message, and wait for the user to
            # press 'enter'. To pause the loop and print the list x,
            # remove the # from the line below:
            #input(x)

            # This is the end of the loop. The next lines only run after the
            # loop is finished.

        # See https://matplotlib.org/3.1.0/tutorials/introductory/pyplot.html
        # For more on plotting with matplotlib.pyplot
        plt.figure()
        plt.plot(x, sin)
        plt.plot(x, cos)
        plt.show(block=False)

###############################################################################
# These next lines 'call' the functions defined above.
# If you erase the lines below (or put a # in front of them) this code won't
# 'do' anything (it won't generate graphs anymore.)
plot_without_pandas()
input("Press enter to close the graphs and end the program")
