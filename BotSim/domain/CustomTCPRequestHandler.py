'''
Created on Dec 13, 2013

@author: root
'''

from threading import Thread, Event

class CustomTCPRequestHandler(Thread):    
    '''
    classdocs
    '''
    __stopEvent = Event()

    def __init__(self, socket, address):
        '''
        Constructor
        '''
        Thread.__init__(self)
        self.address = address
        self.socket = socket
        
    
    def run(self):
        self.socket.recv(1024)        
        self.socket.send("Hi client\n")   
        
    def stop(self):
        self.__stopEvent.set()
        
    def stopped(self):
        return self.__stopEvent.isSet()     
    