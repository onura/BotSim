'''
Created on Dec 20, 2013

@author: Onur
'''

class FeatureModule(object):
    """ An abstract class for runnable feature modules.
        
        This class is the base class for all runnable 
        feature modules. It involves the most basic methods
        of a runnable feature module.
        
        Attributes:
            __name: Name of the module (ex: DDoS Module)
            __results: The results of the module operation can 
                be found here.
    """
    
    __name = None
    __results = None

    def __init__(self, name):
        """ Initializes with a module name."""
        self.__name = name
        self.__results = []
    
    def start(self, *args):
        """ Start method of a module. It has to be implemented
            by every feature module. """
        raise NotImplementedError("Start method should be implemented.")
    
    def stop(self):
        """ Stop method of a module. It has to be implemented
            by every feature module. """
        raise NotImplementedError("Stop method should be implemented.")

    def getResults(self):
        """ Returns the list of results."""
        return list(self.__results)