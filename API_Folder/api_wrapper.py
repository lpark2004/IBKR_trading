"""
Has the functions necessary to start communication with the api
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper  

class IBapi(EWrapper, EClient):
     def __init__(self):
         EClient.__init__(self, self) 

app = IBapi()
app.connect('192.168.1.28', 7947, 1230)
app.run()


#Uncomment this section if unable to connect
#and to prevent errors on a reconnect
import time
time.sleep(5)
app.disconnect()
