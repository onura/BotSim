'''
Created on Dec 20, 2013

@author: root
'''

class FeatureModule(object):
    '''
    classdocs
    '''
    
    __name = None
    __results = None

    def __init__(self, name):
        '''
        Constructor
        '''
        self.__name = name
        self.__results = []
    
    def start(self, *args):
        raise NotImplementedError("This method should be implemented.")
    
    def stop(self):
        raise NotImplementedError("This method should be implemented.")

    def getResults(self):
        return list(self.__results)