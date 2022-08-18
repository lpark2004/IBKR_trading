'''
Building a robust backtester
'''

import os

class Backtest:

    def __init__(self, start_money):
        
        self.data = os.listdir("C:/Users/lukep/Documents/Coding_Projects/Algo_Trading_Data/papertradingdata")
        self.start_money = start_money
        self.total_return = 0
        self.sharpe_ratio = 1
        self.drawdown = 0
        self.total_trades = 0
        self.win_rate = 0
        self.lose_rate = 0
        self.trades = []

        self.on_all()

    def on_slice(self, slice, file_name):


        return None

    def on_day(self, file):
        self.calls_asks_velocities = []
        self.calls_asks_short_momentum = []
        self.calls_asks_long_momentum = []
        self.calls_asks_impulse_short = []
        self.calls_asks_impulse_long = []

        self.calls_bidss_velocities = []
        self.calls_bidss_short_momentum = []
        self.calls_bids_long_momentum = []
        self.calls_bids_impulse_short = []
        self.calls_bids_impulse_long = [] 

        self.puts_asks_velocities = []
        self.puts_asks_short_momentum = []
        self.puts_asks_long_momentum = []
        self.puts_asks_impulse_short = []
        self.puts_asks_impulse_long = [] 

        self.puts_bids_velocities = []
        self.puts_bids_short_momentum = []
        self.puts_bids_long_momentum = []
        self.puts_bids_impulse_short = []
        self.puts_bids_impulse_long = []       
        
        return None

    def on_all(self):
        
        return None

    #return functions
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

    

    
