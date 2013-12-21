'''
Created on Dec 22, 2013

@author: Onur
'''

from domain.TCPClient import TCPClient
from domain.Bot import Bot
from domain import BotConfig

if __name__ == '__main__':
    bot = Bot(TCPClient(BotConfig.SERVER_IP, BotConfig.SERVER_PORT))
    bot.activate()