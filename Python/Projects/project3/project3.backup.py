"""Import statements tell python what packages you'll be using.

You can use 'as' to change how you refer to the package. In this file,
I import matplotlib.pyplot as plt so I don't have to type out
'matplotlib.pyplot' every time I want to use it.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###############################################################################
"""After the import statements, I define one function: plot_with_pandas.
Function definitions start with the word 'def' and end when
the indentation ends. For example:


def ex1():
    print("This line is part of the function 'ex1' because it's indented")

    print("This line is still part of the function 'ex1'")
    print("Blank lines do not end the current level of indentation")

print("This line is not part of the function 'ex1' because it's not indented")


"""


def plot_with_pandas():
    """Generate plot, using pandas."""
    # pandas has an easy way to read csv data.
    # you can use pd.read_csv(), with a string that
    # tells pandas where to find the data file.
    # See https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    # for full documentation.
    df = pd.read_csv("inputs/data.csv")

    # Now, there's a pandas dataframe named 'df' that holds all the information
    # that was in inputs/data.csv
    # A dataframe is a container we can store data in. For now, you can
    # visualize it as a table, or a spreadsheet in excel.

    # Dataframes come with their own built-in way to generate graphs.
    # This next line will generate a graph that plots the x column along the
    # x axis, and the sin and cos columns on the y-axis.
    df.plot(x="x", y=["sin", "cos"])

    # Pandas uses matplotlib.pyplot to generate graphs so you don't have to
    # interact with matplotlib.pyplot directly. In the next line, we DO interact
    # with matplotlib.pyplot directly to show the graph. We set block=False
    # because otherwise, our program will pause here until the graph is shown.
    # Instead, our program continues to run until the line below that
    # starts with 'input'
    # input() will print a string (a string is just text with quotes
    # around it) and wait for the user to press enter.
    plt.show(block=False)


def generate_new_data():
    """Generate new data."""
    # In this function, I'll show you how I generated the input.csv file you
    # used in project 1 and 2.
    x = np.linspace(0, 100, 1000)
    # you can look at x by removing the '#' at the beginning of the line below:
    #print(x)
    y = np.linspace(0, 100, 1000)
    # you can look at y by removing the '#' at the beginning of the line below:
    #print(y)

    # More complicated data can be generated with loops
    # First, create an empty list
    sin = []
    # Then, loop thorugh x, change each value of x in some way, and add it to
    # the end of the list.
    for i in x:
        changed_value = np.sin(i)
        # append means 'add to the end'
        sin.append(changed_value)

    # you can look at sin by removing the '#' at the beginning of the line below:
    #print(sin)

    # np.sin() and np.cos() allow you to calculate the sine and cosine of
    # more than one value at a time
    cos = np.cos(x)
    # you can look at cos by removing the '#' at the beginning of the line below:
    #print(cos)

    # To easily write data to a csv, make a pandas dataframe.
    # first, create a dictionary of the data. For this example,
    # the dictionary can be thought of as an excel spreadsheet, where the 'key'
    # is the column header, and the :value is the data in the column.
    temp_dictionary = {'x' : x,
                       'y' : y,
                       'sin' : sin,
                      'cos' : cos}

    # then, use the dictionary to create the dataframe
    df = pd.DataFrame(temp_dictionary)

    # dataframes can be written to csv files directly
    df.to_csv("inputs/data.csv", index=False)


###############################################################################
# These next lines 'call' the functions defined above.
# If you erase the lines below (or put a # in front of them) this code won't
# 'do' anything (it won't generate a graph anymore.)
generate_new_data()
plot_with_pandas()

input("Press enter to close the graph (if it's still open) and end the program")

# This program is broken into three parts:
# Part 1 pulls in (imports) code that other people wrote.
# Part 2 defines a function that you'll be using later.
#     Our function, plot_with_pandas, is really only 3 lines of running code,
#     but defining a function allows us to use those 3 lines together, without
#     having to re-type them every time we want them to run.
# Part 3 is the 'execution' part. It's the part that python actually 'does'.
# It runs the function defined in part 2, then it pauses on the input line until
# the user (you) hits enter.
