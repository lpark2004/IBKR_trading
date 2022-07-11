"""
This file will handle the automated nature of this task
"""

import pandas_market_calendars as mcal
import sched
import time
import datetime
import pytz
import pause


now = datetime.datetime.now(pytz.timezone('US/Eastern'))
date = now.date()
date_total = now.strftime("%d/%m/%Y %H:%M")
day = now.strftime("%d")
month = now.strftime("%m")
year = now.strftime("%Y")
hour = now.strftime("%H")
minute = now.strftime("%M")
print(day)
print(month)
print(year)
print(hour)
print(minute)
print(date_total)
print(date)

#tomorrow = date + datetime.timedelta(days = 7)
#print(tomorrow)
#nyse = mcal.get_calendar('NYSE')

"""
while True:
    now = datetime.datetime.now(pytz.timezone('US/Eastern'))
    date_today = now.date()
    day = now.strftime("%d")
    month = now.strftime("%m")
    year = now.strftime("%Y")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    date_next_week = date_today + datetime.timedelta(days = 7)




    

    open_day = nyse.valid_days(start_date = str(date_today), end_date = str(date_today))
        if len(open_day) == 0 or (minute >= 30 and hour >= 6):
            next_trading_day = str(nyse.valid_days(start_date = str(date_today). end_date = str(date_next_week))[0])
            



print(nyse)
"""
