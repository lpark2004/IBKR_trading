import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
import math
from datetime import datetime

def file_opener(file):
    '''
    opens pickle files
    '''
    new_file = open(file, "rb")
    objects = []
    objects.append(pickle.load(new_file))

    return objects

def simple_graph(list):
    x = [index for index in range(len(list))]
    y = list
    plt.plot(x,y)
    plt.show()

training_data = file_opener("/Users/lukepark/Documents/training_data.pickle")

simple_graph(training_data[0][0]['calls_bids_short_momentum'])

