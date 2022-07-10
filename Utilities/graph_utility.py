"""
This file contains several graphing functions to help visualize data
"""
import matplotlib.pyplot as plt
import matplotlib

def simple_graph(list):
    x = [index for index in range(len(list))]
    y = list
    plt.plot(x,y)
    plt.show()