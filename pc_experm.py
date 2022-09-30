# %%
import matplotlib
import sklearn

from Utilities import graph_utility as graph
from Utilities import general_utilities as gen_util

#graphical analysis

training_data = gen_util.file_opener("C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/training_data/training_data.pickle")[0]

day_1 = training_data[0]

prices = ["calls_asks", "puts_asks"]
parameters = [ "calls_asks_long_momentum", "calls_asks_short_momentum"]

graph.multi_graph(day_1, prices, parameters)


# %%
'''

training_data = gen_util.file_opener("C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/training_data/training_data.pickle")[0]



for day in training_data:
    for key in day.keys():
        if (key == 'file_data' or key == 'calls_asks_long_impulse'):
            del day[key]
'''




    
    



'''
import os
import sys

sys.path.insert(0, 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading/Backtester')

from backtest import*
from slice import*
#testing splice class

file_path = 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/fixed_data/01Apr2021.pickle'
slice_object = Slice(file_path, 1000, 'calls')
print(slice_object.ask())
'''



