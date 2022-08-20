'''
fixing all of the pickle data into a dictionary structure
'''

import pickle
import os
import sys

sys.path.insert(0, 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading/Utilities')

from general_utilities import file_opener

#get the file paths for everything inside of the papertrading_directory
file_path = 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/papertradingdata'
dir_list = os.listdir(file_path)

#creating a directory list of all files with all wanted variables
complete_data = []
for file_name in dir_list:
    file = file_opener(file_path + "/" + file_name) 
    if len(file[0]) == 32:
        complete_data.append(file_path + '/' + file_name)

#changes file format to the new format
#file keys are as follows
#calls_bids, puts_bids, calls_asks, puts_asks, time_stamps, calls_volumes, puts_volumes, calls_bids_sizes, puts_bids_sizes, calls_asks_sizes, puts_asks_sizes
def change_file(file_name):
    file_data = file_opener(file_name)[0]
    file_dict = {'calls_bids': file_data[0][0], 'puts_bids': file_data[0][1], 'calls_asks': file_data[1][0], 'puts_asks': file_data[1][1], 'time_stamps': file_data[2], 'calls_volumes': file_data[29][0], 'puts_volumes': file_data[29][1], 'calls_bids_sizes': file_data[30][0], 'puts_bids_sizes': file_data[30][1], 'calls_asks_sizes': file_data[31][0], 'puts_asks_sizes': file_data[31][1]}

    out_path = 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/fixed_data/'
    file_name = out_path + file_name[-16:]
    outfile = open(file_name, 'wb')
    pickle.dump(file_dict, outfile)
    outfile.close

#changes all of the files in the complete data list
for file in complete_data:
    change_file(file)
