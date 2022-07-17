"""
Has the functions necessary to communicate with the api
"""

from ibapi.wrapper import *
from ibapi.client import *
from ibapi.contract import *
from ibapi.order import *
from threading import Thread
import queue
import datetime
import time
import math

'''
How communication with IBKR API is established

Code --> IBKR API --> IBKR Server
IBKR Server --> IBKR API --> Code

Send messages to TWS --> Use Client Class
Receive messages from TWS --> Use Wrapper Class
'''

#TestWrapper is a class meant to handle incoming messages from IB servers
#This class is inherited from EWrapper and overrides its default return methods
#In order to make handling and processing easier
class TestWrapper(EWrapper):

    #error handling methods
    #API sends messages through errors
    #errors are stored in queue because it is in chronological order
    def init_error(self):
        error_queue = queue.Queue()
        self.my_errors_queue = error_queue
    
    #if there is a non empty error
    #returns true
    def is_error(self):
        error_exist = not self.my_errors_queue.empty()
        return error_exist

    #try except loop that gets the error message based on is_error
    def get_error(self, timeout=6):
        if self.is_error():
            try:
                return self.my_errors_queue.get(timeout=timeout)
            except queue.Empty:
                return None
        return None

    #overrides error method in the API files to produce a message that is 
    #easier to read
    def error(self, id, errorCode, errorString):
        ## Overrides the native method
        errormessage = "IB returns an error with %d errorcode %d that says %s" % (id, errorCode, errorString)
        self.my_errors_queue.put(errormessage)

    #adding robustness to messages from server
    #asking for server time to prove connection
    #time handling methods
    def init_time(self):
        time_queue = queue.Queue()
        self.my_time_queue = time_queue
        return time_queue

    #put the server_time into our time_queue
    def currentTime(self, server_time):
        ## Overriden method
        self.my_time_queue.put(server_time)

#TestClient is used by the API to send messages to the server
#In this class we do not override methods
#Test Client is just used to invoke messagesa nd requests
class TestClient(EClient):

    def __init__(self, wrapper):
        #Set up with a wrapper inside
        EClient.__init__(self, wrapper)

    #invokes a time request from the server
    def server_clock(self):

        print("Asking server for Unix time")

        #Creates a queue to store the time
        time_storage = self.wrapper.init_time()

        #Sets up a request for unix time from the Eclient
        self.reqCurrentTime()

        #Specifies a max wait time if there is no connection
        max_wait_time = 10

        #try except used in case connection problems
        try:
            requested_time = time_storage.get(timeout = max_wait_time)
        except queue.Empty:
            print("THe queue was empty or max time reached")
            requested_time = None

        #checks if there are any error messages 
        while self.wrapper.is_error():
            print("Erorr:")
            print(self.get_error(timeout=5))

        return requested_time

#TestApp class is where we establish environmental variables
#Primarily used to implement the TestWrapper and TestClient classes
#and begins the server connection
class TestApp (TestWrapper, TestClient):
    #Initializes our main classes
    def __init__(self, ipaddress, portid, clientid):
        TestWrapper.__init__(self)
        TestClient.__init__(self, wrapper = self)

        #Connects to the server with the ipaddress, portid, and clientId specified in
        #the program execution area
        self.connect(ipaddress, portid, clientid)

        #Initializes the threading
        thread = Thread(target = self.run)
        thread.start()
        setattr(self, "_thread", thread)

        #Starts listening for errors
        self.init_error()


if __name__ == '__main__':

    print("before start")
 
    # Specifies that we are on local host with port 7497 (paper trading port number)
    app = TestApp("127.0.0.1", 7497, 0)
 
    # A printout to show the program began
    print("The program has begun")
 
    #assigning the return from our clock method to a variable
    requested_time = app.server_clock()
 
    #printing the return from the server
    print("This is the current time from the server " )
    print(requested_time) 