# Author: Navin
# Created: December 2020
# License: MIT
 
# Installation instructions:
# It is recommended that you install Python as part of a virtual environment like pyEnv so that it does not mess up your system's Python. Python3 is preferred.
# Install dependent libraries:
# >>> pip3 install pygame
# >>> pip3 install pymunk
# Now simply run using: 
# >>> python3 main.py

import os
import logging, traceback
from Parameters import BallSizes
from Environment import *

class MainSimulator(object):
    def __init__(self):
        self.worlds = []
        self.worldOrdinal = -1        
        #---registration of the environments
        self.worlds.append(Environment(BallSizes.MEDIUM))
        self.worlds.append(Environment(BallSizes.SMALL))
        self.worlds.append(Environment(BallSizes.LARGE))   
    
    def nextSim(self):
        self.worldOrdinal += 1
        if self.worldOrdinal < len(self.worlds):
            w = self.worlds[self.worldOrdinal]
            w.initialize()
            #time.sleep(5)
            w.runWorld()
        return self.worldOrdinal < len(self.worlds)#any more worlds to process?

#-----------------------------------------------
#-----------------------------------------------
#             PROGRAM STARTS HERE
#-----------------------------------------------
#-----------------------------------------------
if __name__ == '__main__':
    noErrors = True
    sim = MainSimulator()    
    
    try:
        if sim != None:
            while sim.nextSim():
                pass
    except BaseException as e:
        noErrors = False
        print(e)
        logging.error(traceback.format_exc(None, True))  
