'''
defines what a dataslice looks like
'''
import sys
import os

sys.path.insert(0, 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading/Utilities')
from general_utilities import file_opener

class Slice:
    
    def __init__(self, file_path, position_stamp, type):
        self.file = file_opener(file_path)
        self.position = position_stamp

    def ask(self):
        return self.file[0][0][0][self.position]
    
    def bid(self):