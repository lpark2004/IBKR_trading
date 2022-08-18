"""
general utility functions needed throughout the scope of this project
"""
import pickle
import os

#returns everything inside of a pickle file
def file_opener(file):
    '''
    opens pickle files
    '''
    new_file = open(file, "rb")
    objects = []
    objects.append(pickle.load(new_file))

    return objects

