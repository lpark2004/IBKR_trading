'''
Has the methods needed for creating an order
'''

from ibapi.wrapper import *
from ibapi.client import *
from ibapi.contract import *
from ibapi.order import *
from threading import Thread
import queue
import datetime
import time
import math

#Building a contract object

def contractCreate(symbol, secType, exchange):
    #Fills out the contract object
    contract1 = Contract() #Creates a contract object form the import
    contract1.symbol = symbol #Sets the ticker symbol
    contract1.secType = secType #Defines the security type as stock
    contract1.currency = "USD" #Currency is US dollars
    contract1.exchange = exchange

    return contract1 #Returns the contract object

def orderCreate(action, orderType, totalQuantity):
    #Fills out the order object
    order1 = Order()    #Creates an order object from the import
    order1.action = action   #Sets the order action to buy
    order1.orderType = orderType    #Sets order type
    order1.transmit = True
    order1.totalQuantity = totalQuantity  #Amount of shares being purhcased
    
    return order1

'''
def orderExecution():

    #Places the order with the returned contract and order objects
    contractObject = contractCreate("AAPL", "STK", "SMART")
    orderObject = orderCreate("BUY", "MKT", 1)
    nextID = 101
    app.placeOrder(nextID, contractObject, orderObject)
'''
