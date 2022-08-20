'''
defines what a dataslice looks like
'''
import sys
import os

sys.path.insert(0, 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading/Utilities')
from general_utilities import file_opener

class Slice:
    
    def __init__(self, file_path, position_stamp, type):
        self.file = file_opener(file_path)[0]
        self.position = position_stamp
        self.type = type

    def ask(self):
        return self.file[self.type + '_asks'][self.position]
    
    def bid(self):
        return self.file[self.type + '_bids'][self.position]

    def asks_sizes(self):
        return self.file[self.type + '_asks_sizes'][self.position]

    def bids_size(self):
        return self.file[self.type + '_bids_sizes'][self.position]

    def delta_volume(self):
        if self.position == 0:
            return 0
        elif self.position != 0:
            return (self.file[self.type + '_volumes'][self.position] - self.file[self.type + '_volumes'][self.position - 1])

    def prev_ask(self):
        if self.position != 0:
            return self.file[self.type + '_asks'][self.position - 1]
        elif self.position == 0:
            return 0
    
    def prev_bid(self):
        if self.position != 0:
            return self.file[self.type + '_bids'][self.position - 1]
        elif self.position == 0:
            return 0