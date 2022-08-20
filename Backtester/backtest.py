'''
Building a robust backtester
'''

import os
import sys
from collections import deque


sys.path.insert(0, 'C:/Users/lukep/Documents/Coding_Projects/Algo_Trading/Utilities')

from indicators import* 
from general_utilities import*
from slice import Slice

class Backtest:
    #class variables
    Securities = []
    Portfolio = []
    Trades = []


    def __init__(self):
        
        self.path = "C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/fixed_data"
        self.data = os.listdir(self.path)
        self.start_money = 10000
        
        self.on_all()

    '''
    event handlers
    '''
    #what to do on a second by second basis
    def on_slice(self, call, put):
        
        return None

    #what to do daily with data in backtest
    def on_day(self, file):
        self.calls_asks_velocities = [0]
        self.calls_asks_short_momentum = deque()
        self.calls_asks_long_momentum = deque()
        self.calls_asks_impulse_short = deque()
        self.calls_asks_impulse_long = deque()

        self.calls_bidss_velocities = [0]
        self.calls_bidss_short_momentum = deque()
        self.calls_bids_long_momentum = deque()
        self.calls_bids_impulse_short = deque()
        self.calls_bids_impulse_long = deque()

        self.puts_asks_velocities = [0]
        self.puts_asks_short_momentum = deque()
        self.puts_asks_long_momentum = deque()
        self.puts_asks_impulse_short = deque()
        self.puts_asks_impulse_long = deque()

        self.puts_bids_velocities = [0]
        self.puts_bids_short_momentum = deque()
        self.puts_bids_long_momentum = deque()
        self.puts_bids_impulse_short = deque()
        self.puts_bids_impulse_long = deque()

        self.todays_data = file_opener(self.path + '/' + file)

        for second in range(len(self.todays_data['calls_asks'])):
            self.slice_calls = Slice(self.todays_data, second, 'calls')
            self.slice_puts = Slice(self.todays_data, second, 'puts')
            self.on_slice(self.slice_calls, self.slice_puts)

        return None
    
    #calls all of the data that needs to be backtested
    def on_all(self):
        for day in self.data:
            self.on_day(day)
        
        return None
    
    def on_end_of_day(self):
        return None

    '''
    return functions
    '''
    def log(self):
        return self.log

    def total_return(self):
        return self.total_return

    def sharpe_ratio(self):
        return self.sharpe_ratio

    def total_trades(self):
        return self.total_trades

    def win_rate(self):
        return self.win_rate

    def lose_rate(self):
        return self.lose_rate

    def drawdown(self):
        return self.drawdown

backtest_result = Backtest(10000)

    

    
