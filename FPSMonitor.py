import pygame, datetime
from createText import createText
pygame.init()

## FPS monitor for the game
class FPSCounter:
    def __init__(self,surf,displayInWindow=False,displayInTerminal=False):
        self.sec = datetime.timedelta(seconds=1)
        self.frames = 0
        self.nextFPStime = datetime.datetime.today() + self.sec
        self.framesText = createText(f"FPS: {self.frames}","bahnschrift",(255,255,255),20)
        self.displayInWindow = displayInWindow
        self.displayInTerminal = displayInTerminal

    ## Updates the FPS and text surface
    def update(self,surf,pixelChange=1):
        
        self.frames += 1
        
        if self.nextFPStime <= datetime.datetime.today():
            
            if self.displayInTerminal == True:
                print(self.frames)
            
            if self.displayInWindow == True:
                self.framesText = createText(f"FPS: {self.frames}","bahnschrift",(255,255,255),int(30*pixelChange))
            
            
            self.frames = 0
            self.nextFPStime = datetime.datetime.today() + self.sec
        
        if self.displayInWindow == True:
            surf.blit(self.framesText,(int(10*pixelChange),int(3*pixelChange)))