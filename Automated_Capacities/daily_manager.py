"""
This file will handle the automated nature of this task
"""

import pandas_market_calendars as mcal
import sched
import time
import datetime
import pytz
import pause
import pickle 

nyse = mcal.get_calendar('NYSE')
#data_path = "C:\Users\Luke Park\Documents\IBKR_trading\data"

#time right now in New York
now = datetime.datetime.now(pytz.timezone('US/Eastern'))
date_today = now.date()
hour = now.hour
minute = now.minute
date_next_week = date_today + datetime.timedelta(days = 7)

#time difference between datetime default and Eastern time
time_dif = 3


open_day = nyse.valid_days(start_date = str(date_today), end_date = str(date_today))

#if today is not a valid training day, or it is past market open time, wait until next trading day
if len(open_day) == 0 or hour > 6 or (minute >= 30 and hour == 6):
    next_trading_day = nyse.valid_days(start_date = str(date_today), end_date = str(date_next_week))[0]
    ntd = next_trading_day
    next_trading_day = datetime.datetime(ntd.year, ntd.month, ntd.day, 9 - time_dif, 20)
    pause.until(next_trading_day)
    


#if today is a valid training day and market has not opened yet
elif len(open_day) != 0 and (hour == 6 and minute < 30):
    file_name = str(now.strftime('%d%b%Y')) + ".pickle"

file_name = str(now.strftime('%d%b%Y')) + ".pickle"
print(file_name)


"""
while True:
    nyse = mcal.get_calendar('NYSE')

    #time right now in New York
    now = datetime.datetime.now(pytz.timezone('US/Eastern'))
    date_today = now.date()
    hour = now.hour
    minute = now.minute
    date_next_week = date_today + datetime.timedelta(days = 7)

    #time difference between datetime default and Eastern time
    time_dif = 3


    open_day = nyse.valid_days(start_date = str(date_today), end_date = str(date_today))

    #if today is not a valid training day, or it is past market open time, wait until next trading day
    if len(open_day) == 0 or hour > 6 or (minute >= 30 and hour == 6):
        next_trading_day = nyse.valid_days(start_date = str(date_today), end_date = str(date_next_week))[0]
        ntd = next_trading_day
        next_trading_day = datetime.datetime(ntd.year, ntd.month, ntd.day, 9 - time_dif, 20)
        pause.until(next_trading_day)
        continue

    #if today is a valid training day and market has not opened yet
    #elif len(open_day) != 0 and (hour == 6 and minute < 30):
"""









