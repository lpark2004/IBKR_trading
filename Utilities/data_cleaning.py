import general_utilities as gen_util
import graph_utility as graph_util
import indicators as ind
import os

path = 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/fixed_data'

file_list = [path + '/' + x for x in os.listdir(path)]



#'calls_bids', 'puts_bids', 'calls_asks', 'puts_asks', 'time_stamps', 'calls_volumes',
#'puts_volumes', 'calls_bids_sizes', 'puts_bids_sizes', 'calls_asks_sizes', 'puts_asks_sizes'

#variables to make

'''
calls_asks_velocities = ind.vel_list(file['calls_asks'])
calls_asks_short_momentum = [0 for num in range(60)] + [ind.weighted_momentum(calls_asks_velocities[0:num], 60) for num in range(60, len(calls_asks_velocities))]
calls_asks_long_momentum = [0 for num in range(300)] + [ind.weighted_momentum(calls_asks_velocities[0:num], 300) for num in range(300, len(calls_asks_velocities))]
calls_asks_impulse_short = [0 for num in range(60)] + [ind.simple_momentum(calls_asks_short_momentum[0:num], 60) for num in range(60, len(calls_asks_short_momentum))]
calls_asks_impulse_long = [0 for num in range(60)] + [ind.simple_momentum(calls_asks_long_momentum[0:num], 60) for num in range(60, len(calls_asks_long_momentum))]

calls_bids_velocities = ind.vel_list(file['calls_bids'])
calls_bids_short_momentum = [0 for num in range(60)] + [ind.weighted_momentum(calls_bids_velocities[0:num], 60) for num in range(60, len(calls_bids_velocities))]
calls_bids_long_momentum = [0 for num in range(300)] + [ind.weighted_momentum(calls_bids_velocities[0:num], 300) for num in range(300, len(calls_bids_velocities))]
calls_bids_impulse_short = [0 for num in range(60)] + [ind.simple_momentum(calls_bids_short_momentum[0:num], 60) for num in range(60, len(calls_bids_short_momentum))]
calls_bids_impulse_long = [0 for num in range(60)] + [ind.simple_momentum(calls_bids_long_momentum[0:num], 60) for num in range(60, len(calls_bids_long_momentum))]

'''

def preprocessing(file):

    calls_asks_velocities = ind.vel_list(file['calls_asks'])
    calls_asks_short_momentum = [0 for num in range(60)] + [ind.weighted_momentum(calls_asks_velocities[0:num], 60) for num in range(60, len(calls_asks_velocities))]
    calls_asks_long_momentum = [0 for num in range(300)] + [ind.weighted_momentum(calls_asks_velocities[0:num], 300) for num in range(300, len(calls_asks_velocities))]
    calls_asks_impulse_short = [0 for num in range(60)] + [ind.simple_momentum(calls_asks_short_momentum[0:num], 60) for num in range(60, len(calls_asks_short_momentum))]
    calls_asks_impulse_long = [0 for num in range(60)] + [ind.simple_momentum(calls_asks_long_momentum[0:num], 60) for num in range(60, len(calls_asks_long_momentum))]

    calls_bids_velocities = ind.vel_list(file['calls_bids'])
    calls_bids_short_momentum = [0 for num in range(60)] + [ind.weighted_momentum(calls_bids_velocities[0:num], 60) for num in range(60, len(calls_bids_velocities))]
    calls_bids_long_momentum = [0 for num in range(300)] + [ind.weighted_momentum(calls_bids_velocities[0:num], 300) for num in range(300, len(calls_bids_velocities))]
    calls_bids_impulse_short = [0 for num in range(60)] + [ind.simple_momentum(calls_bids_short_momentum[0:num], 60) for num in range(60, len(calls_bids_short_momentum))]
    calls_bids_impulse_long = [0 for num in range(60)] + [ind.simple_momentum(calls_bids_long_momentum[0:num], 60) for num in range(60, len(calls_bids_long_momentum))]


    calls_volume_delta = ind.vel_list(file['calls_volumes'])
    calls_spread = [file['calls_asks'][num] - file['calls_bids'][num] for num in range(len(file['calls_asks']))]



    puts_asks_velocities = ind.vel_list(file['puts_asks'])
    puts_asks_short_momentum = [0 for num in range(60)] + [ind.weighted_momentum(puts_asks_velocities[0:num], 60) for num in range(60, len(puts_asks_velocities))]
    puts_asks_long_momentum = [0 for num in range(300)] + [ind.weighted_momentum(puts_asks_velocities[0:num], 300) for num in range(300, len(puts_asks_velocities))]
    puts_asks_impulse_short = [0 for num in range(60)] + [ind.simple_momentum(puts_asks_short_momentum[0:num], 60) for num in range(60, len(puts_asks_short_momentum))]
    puts_asks_impulse_long = [0 for num in range(60)] + [ind.simple_momentum(puts_asks_long_momentum[0:num], 60) for num in range(60, len(puts_asks_long_momentum))]

    puts_bids_velocities = ind.vel_list(file['puts_bids'])
    puts_bids_short_momentum = [0 for num in range(60)] + [ind.weighted_momentum(puts_bids_velocities[0:num], 60) for num in range(60, len(puts_bids_velocities))]
    puts_bids_long_momentum = [0 for num in range(300)] + [ind.weighted_momentum(puts_bids_velocities[0:num], 300) for num in range(300, len(puts_bids_velocities))]
    puts_bids_impulse_short = [0 for num in range(60)] + [ind.simple_momentum(puts_bids_short_momentum[0:num], 60) for num in range(60, len(puts_bids_short_momentum))]
    puts_bids_impulse_long = [0 for num in range(60)] + [ind.simple_momentum(puts_bids_long_momentum[0:num], 60) for num in range(60, len(puts_bids_long_momentum))]


    puts_volume_delta = ind.vel_list(file['puts_volumes'])
    puts_spread = [file['puts_asks'][num] - file['puts_bids'][num] for num in range(len(file['puts_asks']))]

price_list = ['calls_asks', 'puts_asks']
param_list = ['puts_asks_long_momentum']

graph_util.multi_graph(gen_util.file_opener(file_list[1])[0], price_list, param_list)
