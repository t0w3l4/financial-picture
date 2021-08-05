"""
Purpose: Update and plot how investments are going.
Inputs:
Outputs:
Author: t0w3l4
Date: August 4, 2021
References:
https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-list-in-python
"""

# Import module for graphing
import matplotlib.pyplot as graph

# Function that will plot the graph


def plot_my_graph():
    my_file = open("Text files/test_investing.txt", "r")
    content = my_file.read()

    # Return list of each date
    content_list = content.split("\n")

    # Initialize empty lists which will have the contribution dates, contribution amounts, and interest amounts inside respectively
    contr_dt = []
    contr_amt = []
    intr_amt = []

    # Remove first line describing format of text file
    del content_list[0]
    # Check if last element in list is empty and removes it if it is
    if content_list[-1] == '':
        del content_list[-1]

    # Loop through each contribution to separate the different data points
    for contribution in content_list:
        # Create a list of elements by splitting the string at the comma ,
        temp_list = contribution.split(',')
        contr_dt.append(temp_list[0])
        # Need to convert strings into floats before plotting
        contr_amt.append(float(temp_list[1]))
        intr_amt.append(float(temp_list[2]))

    # Plot contributions
    graph.plot(contr_dt, contr_amt, label="Contributions")

    # Plot interest
    graph.plot(contr_dt, intr_amt, label="Interest")

    # Labelling the graph
    graph.xlabel('Date')
    graph.xticks(rotation=90)  # Make the x-axis labels vertical
    graph.ylabel('Dollars (CAD)')

    # Adding title to graph
    graph.title('Investment graph')

    # Add a legend to the graph
    graph.legend()

    # Show the graph once it is done
    graph.show()

    # Close the file once done with it
    my_file.close()


plot_my_graph()
