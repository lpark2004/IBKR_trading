import matplotlib

from Utilities import graph_utility as graph
from Utilities import general_utilities as gen_util

training_data = gen_util.file_opener("C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/training_data/training_data.pickle")[0]

day_1 = training_data[0]

prices = ["calls_asks", "puts_asks"]
parameters = ["calls_asks_short_momentum", "calls_asks_long_momentum"]

graph.multi_graph(day_1, prices, parameters)

