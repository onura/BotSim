'''
Created on Dec 22, 2013

@author: Onur
'''

from domain.HTTPClient import HTTPClient
from domain.Bot import Bot
from domain import BotConfig

if __name__ == '__main__':
    bot = Bot(HTTPClient(BotConfig.SERVER_IP, BotConfig.SERVER_PORT))
    bot.activate()