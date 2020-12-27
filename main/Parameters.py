# Author: Navin
# Created: December 2020
# License: MIT

class BallSizes:
    SMALL = 3
    MEDIUM = 5
    LARGE = 8

class RunCode:
    CONTINUE = 1
    STOP = 0
    
class Env:
    screenWidth = 1000
    screenHeight = 800    
    boundaryThickness = 10    
    worldX = 0
    worldY = 0 
    slotHeight = 0.35 * screenHeight
    gapBetweenSlots = 25
    slotThickness = 2    
    pinStartY = 0.10 * screenHeight
    pinRadius = 5
    gapBetweenPins = 30
    boundaryColor = 100,100,100
    slotColor = 50,50,50
    pinColor = 70,69,73
    maxBallsSmall = 500
    maxBallsMedium = 300
    maxBallsLarge = 100
    ballColor = 0, 180, 0
    ballReleaseX = screenWidth/2 + 5
    ballReleaseY = worldY + (boundaryThickness*2)
    ballCreationInterval_seconds = 0.2
    waitTimeToEndSimulation_seconds = 10