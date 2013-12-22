'''
Created on Dec 13, 2013

@author: Onur
'''

from threading import Thread, Event

class CustomTCPRequestHandler(Thread):    
    """ Handles a TCP request
    
        Handles a TCP request without closing the connection.
        There is one request handler per client.
        
        Attributes:
            __stopEvent: A thread event to stop the thread.               
            address: IP,port couple of client
            socket: client connection socket
    """
    __stopEvent = Event()
    address = None
    socket = None

    def __init__(self, socket, address):
        """ Initializes with socket and address which 
            return socket.accept()"""
        Thread.__init__(self)
        self.address = address
        self.socket = socket
        
    
    def run(self):
        """ Gets a hi from the client and sends a hi back
            when a connection has established."""
        self.socket.recv(1024)        
        self.socket.send("Hi client\n")   
        
    def stop(self):
        """ Stops the thread."""
        self.__stopEvent.set()
        
    def stopped(self):
        """ Returns the thread's status."""
        return self.__stopEvent.isSet()     
    