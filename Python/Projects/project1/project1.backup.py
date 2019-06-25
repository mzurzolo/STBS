"""Import statements tell python what packages you'll be using.

You can use 'as' to change how you refer to the package. In this file,
I import matplotlib.pyplot as plt so I don't have to type out
'matplotlib.pyplot' every time I want to use it.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_with_pandas():
    """Generate plot, using pandas."""
    # pandas has an easy way to read csv data.
    # you can use pd.read_csv(), with a string that
    # tells pandas where to find the data file.
    # See https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    # for full documentation.
    df = pd.read_csv("inputs/data.csv")

    df.plot(x='x', y=['sin', 'cos'])
    plt.show()


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
        print(column_names)
        # this will loop through each line in the file
        for line in file:
            # Split each line into a list of values,
            # using a comma as the separation point
            split_line = line.split(",")
            # Add the first value of the split line to our list of x values
            # This will also strip out any extra spaces and convert the value
            # to a number
            x.append(float(split_line[0].strip()))
            # Build up every other list the same way
            y.append(float(split_line[1].strip()))
            sin.append(float(split_line[2].strip()))
            cos.append(float(split_line[3].strip()))

            # If you want to watch the list grow, you can use python's input
            # function. Input will print a message, and wait for the user to
            # press 'enter'. To pause the loop and print the list x,
            # uncomment the next line:
            # input(x)
        # See https://matplotlib.org/3.1.0/tutorials/introductory/pyplot.html
        # For more on plotting with matplotlib.pyplot
        plt.figure()
        plt.plot(sin)
        plt.plot(cos)
        plt.show()


def main():
    """Run both functions that generate plots."""
    plot_with_pandas()
    plot_without_pandas()


if __name__ == "__main__":
    main()
