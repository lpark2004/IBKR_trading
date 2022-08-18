'''
attempt 1 at making a linear regression model for my trading strategy
'''

#general imports
from cmath import inf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

'''
#tensorflow based imports
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
'''


#local imports
sys.path.insert(0, 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading/Utilities')

from general_utilities import file_opener


#importing data
data = file_opener("C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/training_data/training_data.pickle")[0]
vars = list(data[0].keys())

#normalize all of the data
max_list = [0 for x in range(len(vars))]
min_list = [inf for x in range(len(vars))]


for day in data:
    #note that the first key is the date so it does not have a numerical value
    for key in range(1, len(vars)):

        temp_max = max(day[vars[key]])
        temp_min = min(day[vars[key]])

        if (temp_max > max_list[key]):
            max_list[key] = temp_max
        
        if (temp_min < min_list[key]):
            min_list[key] = temp_min

input_data = []
for day in data: 
    days_list = []
    for second in range(len(day[vars[1]])):
        seconds_list = []
        for key in range(1, len(vars)):
            seconds_list.append((day[vars[key]][second] + abs(min_list[key])) / (abs(min_list[key]) + max_list[key]))
        days_list.append(seconds_list)
    input_data.append(days_list)

training_data = np.array(input_data[0:40])
testing_data = np.array(input_data[40:])

