### --------- Defining the window to be used in the Casino game ---------- ###

#So I know this is sort of ugly, but I have a bunch of functions in other files
#that all reference the window (like to draw things onto it), so when splitting my code up
#I just added in window as an optional argument to the end of each function, defaulting it to w
#and then this file has that w that it references.


import pygame, sys
from pygame.locals import *

w = pygame.display.set_mode((1080, 696))
moveType = None
buildChoicesSpots = {0: (24*33,24*25), 1: (24*35,24*25), 2: (24*37,24*25), 3: (24*39,24*25)}
buildRankDict = {0: 0 , 1: 0, 2: 0, 3: 0}

