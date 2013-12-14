'''
Created on Dec 14, 2013

@author: Onur
'''

import socket
#import time


if __name__ == '__main__':
    csock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csock.connect(("localhost", 555))
    csock.send("hi - server\n")
    
    while True:
        data = csock.recv(1024)
        print data