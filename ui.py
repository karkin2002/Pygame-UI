import pygame, time, keyboard, audioplayer
from FPSMonitor import FPSCounter
from createText import createText, createTextBox



##  ------ audioplayer module ------  ##
## Other commands:
##  - play(loop, block) block = stops thread until playback ends
##  - pause()
##  - resume()
##  - stop()
##  - close()
##  - seek(position) = moves playback to specified position

## Returns audio class
def loadAudio(filename):
    return audioplayer.AudioPlayer(filename)

## Sets volume of audio class
def setVolume(audio, value):
    audio.volume = value

## Returns current state of audio (paused, playing, ...)
def getState(audio):
    return audio.state

## Sets speed of playback
def setSpeed(audio, value):
    audio.speed = value

## Returns speed of playback
def getSpeed(audio):
    return audio.speed


## Button
## 3 button types: "toggle", "press", "hold"
## unpressSurface & pressSurface enter as stings
class button:
    def __init__(self, widthDif, x, y, unpressSurface, pressSurface, hoverSurface = None, unpressSurfaceWidth = None, unpressSurfaceHeight = None, pressSurfaceWidth = None, pressSurfaceHeight = None, hoverSurfaceWidth = None, hoverSurfaceHeight = None, buttonType = "press", press = False, pressAudio = None, hoverAudio = None, pressAudioVolume = 50, hoverAudioVolume = 50,   centered = False, display = True):
        self.x = x
        self.y = y

        ## Loading unpressSurace / pressSurface as surfaces
        self.OrinalUnpressSurface = pygame.image.load(unpressSurface)
        self.OrinalPressSurface = pygame.image.load(pressSurface)
        if hoverSurface != None:
            self.OriginalHoverSurface = pygame.image.load(hoverSurface)
        else:
            self.OriginalHoverSurface = None

        ## Setting the width and height of unpressSurface / pressSurface
        if unpressSurfaceWidth != None:
            self.unpressSurfaceWidth = unpressSurfaceWidth
        else: 
            self.unpressSurfaceWidth = self.OrinalUnpressSurface.get_width()

        if unpressSurfaceHeight != None:
            self.unpressSurfaceHeight = unpressSurfaceHeight
        else: 
            self.unpressSurfaceHeight = self.OrinalUnpressSurface.get_height()


        if pressSurfaceWidth != None:
            self.pressSurfaceWidth = pressSurfaceWidth
        else: 
            self.pressSurfaceWidth = self.OrinalPressSurface.get_width()

        if pressSurfaceHeight != None:
            self.pressSurfaceHeight = pressSurfaceHeight
        
        else: 
            self.pressSurfaceHeight = self.OrinalPressSurface.get_height()


        if self.OriginalHoverSurface != None:
            if hoverSurfaceWidth != None:
                self.hoverSurfaceWidth = hoverSurfaceWidth
            
            else:
                self.hoverSurfaceWidth = self.OriginalHoverSurface.get_width()

            if hoverSurfaceHeight != None:
                self.hoverSurfaceHeight = hoverSurfaceHeight
            
            else:
                self.hoverSurfaceHeight = self.OriginalHoverSurface.get_height()



        self.centered = centered
        self.display = display

        self.press = press
        self.hover = False
        self.buttonType = buttonType

        ## Scales images to size of screen
        self.unpressSurface = pygame.transform.scale(self.OrinalUnpressSurface,(round(self.unpressSurfaceWidth * widthDif),round(self.unpressSurfaceHeight * widthDif)))
        self.pressSurface = pygame.transform.scale(self.OrinalPressSurface,(round(self.pressSurfaceWidth * widthDif),round(self.pressSurfaceHeight * widthDif)))
        if self.OriginalHoverSurface != None:
            self.hoverSurface = pygame.transform.scale(self.OriginalHoverSurface,(round(self.hoverSurfaceWidth * widthDif),round(self.hoverSurfaceHeight * widthDif)))
        
        if self.centered == True:
            self.buttonRect = pygame.Rect(round((self.x * widthDif) - self.unpressSurface.get_width()/2), round((self.y* widthDif) - self.unpressSurface.get_height()/2), round(self.unpressSurfaceWidth * widthDif), round(self.unpressSurfaceHeight * widthDif)) # Rect used for collisions, uses unpressedSurfaces size
        else:
            self.buttonRect = pygame.Rect(round(self.x * widthDif), round(self.y * widthDif), round(self.unpressSurfaceWidth * widthDif), round(self.unpressSurfaceHeight * widthDif)) # Rect used for collisions, uses unpressedSurfaces size


        ## Button press audio
        if pressAudio != None:
            self.pressAudio = loadAudio(pressAudio)
            setVolume(self.pressAudio, pressAudioVolume)
        else:
            self.pressAudio = None
        
    
        if hoverAudio != None:
            self.hoverAudio = loadAudio(hoverAudio)
            setVolume(self.hoverAudio, hoverAudioVolume)
        else:
            self.hoverAudio = None




    ## Check collision between mouse and buttonRect
    def collision(self,mousePos):
        return self.buttonRect.collidepoint(mousePos)


    ## Changes press value depending on the button type, mouse pos,
    ## button press and click counter. Returns an update request to
    ## redraw  the window / button
    def checkPress(self, mousePos, mousePress, clickCounter, widthDif, menuCentered, menuX, menuY, width, height):
        updateRequest = False

        if menuCentered == True:
            mousePos = (mousePos[0] - round((menuX - width/2) * widthDif), mousePos[1] - round((menuY - height/2) * widthDif))

        else:
            mousePos = ((mousePos[0] - round(menuX * widthDif)), (mousePos[1] - round(menuY * widthDif)))
        
        if self.display == True:

            ## Button presses
            if mousePress == True:
                if self.buttonType == "toggle":
                    if clickCounter == 1:
                        if self.collision(mousePos):
                            self.press = not self.press
                            updateRequest = True

                            if self.pressAudio != None:
                                self.pressAudio.play()


                elif self.buttonType == "hold":
                    if self.collision(mousePos):
                        if self.press == False:
                            self.press = True
                            updateRequest = True

                elif self.buttonType == "press":
                    if self.press == False and clickCounter == 1:
                        if self.collision(mousePos):
                            self.press = True
                            updateRequest = True
                            
                            if self.pressAudio != None:
                                self.pressAudio.play()
            
            else:
                if self.buttonType == "hold" and self.press == True:
                    self.press = False
                    updateRequest = True
                
                elif self.buttonType == "press" and self.press == True:
                    self.press = False
                    updateRequest = True


            ## Hover surfaces
            if self.OriginalHoverSurface != None:
                if self.collision(mousePos):
                    if self.hover == False:
                        self.hover = True
                        updateRequest = True
                        
                        ## Plays hover audio if hovered
                        if self.hoverAudio != None:
                            self.hoverAudio.play()

                else:
                    if self.hover == True:
                        self.hover = False
                        updateRequest = True

        return updateRequest


    ## Draw button on surface
    def draw(self,surf, widthDif):

        if self.display == True:
            if self.centered == False:
                if self.press == True:
                    surf.blit(self.pressSurface, (round(self.x * widthDif), round(self.y * widthDif)))
                
                else:
                    if self.hover == True:
                        surf.blit(self.hoverSurface, (round(self.x * widthDif), round(self.y * widthDif)))
                    
                    else:
                        surf.blit(self.unpressSurface, (round(self.x * widthDif), round(self.y * widthDif)))
            
            else:
                if self.press == True:
                    surf.blit(self.pressSurface, (round((self.x* widthDif) - self.pressSurface.get_width()/2), round((self.y* widthDif) - self.pressSurface.get_height()/2)))
                
                else:
                    if self.hover == True:
                        surf.blit(self.hoverSurface, (round((self.x* widthDif) - self.hoverSurface.get_width()/2), round((self.y* widthDif) - self.hoverSurface.get_height()/2)))
                    
                    else:
                        surf.blit(self.unpressSurface, (round((self.x* widthDif) - self.unpressSurface.get_width()/2), round((self.y* widthDif) - self.unpressSurface.get_height()/2)))

    
    ## Resuze button images and rect
    def resize(self, widthDif):
        self.unpressSurface = pygame.transform.scale(self.OrinalUnpressSurface,(round(self.unpressSurfaceWidth * widthDif),round(self.unpressSurfaceHeight * widthDif)))
        self.pressSurface = pygame.transform.scale(self.OrinalPressSurface,(round(self.pressSurfaceWidth * widthDif),round(self.pressSurfaceHeight * widthDif)))
        if self.OriginalHoverSurface != None:
            self.hoverSurface = pygame.transform.scale(self.OriginalHoverSurface,(round(self.hoverSurfaceWidth * widthDif),round(self.hoverSurfaceHeight * widthDif)))
        
        if self.centered == True:
            self.buttonRect = pygame.Rect(round((self.x* widthDif) - self.unpressSurface.get_width()/2), round((self.y* widthDif) - self.unpressSurface.get_height()/2), round(self.unpressSurfaceWidth * widthDif), round(self.unpressSurfaceHeight * widthDif)) # Rect used for collisions, uses unpressedSurfaces size
        else:
            self.buttonRect = pygame.Rect(round(self.x * widthDif), round(self.y * widthDif), round(self.unpressSurfaceWidth * widthDif), round(self.unpressSurfaceHeight * widthDif)) # Rect used for collisions, uses unpressedSurfaces size






## Text
class text:
    def __init__(self, widthDif, x, y, text, font, colour, size, centered = False, display = True):
        self.x = x
        self.y = y
        
        self.text = text

        self.font = font
        self.colour = colour
        self.size = size

        self.textSurface = createText(self.text, self.font, self.colour, round(self.size * widthDif))

        self.centered = centered
        self.display = display
            
    ## Draw's text
    def draw(self, surf, widthDif):
        if self.display:
            if self.centered == False:
                surf.blit(self.textSurface, (round(self.x * widthDif), round(self.y * widthDif)))
            
            else:
                surf.blit(self.textSurface, (round((self.x* widthDif) - self.textSurface.get_width()/2), round((self.y* widthDif) - self.textSurface.get_height()/2)))

    def resize(self, widthDif):
        self.textSurface = createText(self.text, self.font, self.colour, round(self.size * widthDif))


## Creates and returns a new surface with a chosen colour and alpha value
def createSurface(widthDif, width, height, surfaceColour, alpha):
    if surfaceColour == None:
        newSurface = pygame.Surface((round(width* widthDif),round(height * widthDif)),pygame.SRCALPHA)
    
    else:
        newSurface = pygame.Surface((round(width* widthDif),round(height * widthDif)))

        if alpha != 255:
            newSurface.set_colorkey((0,0,100))
            newSurface.set_alpha(alpha)
            pygame.draw.rect(newSurface,surfaceColour,(0,0,round(width* widthDif),round(height* widthDif)))
        
        else:
            newSurface.fill(surfaceColour)

    return newSurface





class image:
    def __init__(self, widthDif, x, y, image, width = None, height = None, alpha = 255, centered = False, display = True):
        self.x = x
        self.y = y

        self.OriginalImageSurface = pygame.image.load(image)

        if width != None:
            self.width = width
        else:
            self.width = self.OriginalImageSurface.get_width()

        if height != None:
            self.height = height
        else:
            self.width = self.OriginalImageSurface.get_height()


        self.imageSurface = pygame.Surface((round(self.width * widthDif),round(self.height * widthDif)),pygame.SRCALPHA)
        self.alpha = alpha
        
        if self.alpha != 255:
            self.imageSurface.set_colorkey((0,0,100))
            self.imageSurface.set_alpha(self.alpha)
        
        self.imageSurface.blit(pygame.transform.scale(self.OriginalImageSurface,(round(self.width * widthDif),round(self.height * widthDif))),(0,0))

        self.centered = centered
        self.display = display

    ## Draw Image
    def draw(self, surf, widthDif):
        if self.display:
            if self.centered == False:
                surf.blit(self.imageSurface, (round(self.x * widthDif), round(self.y * widthDif)))
            
            else:
                surf.blit(self.imageSurface, (round((self.x* widthDif) - self.imageSurface.get_width()/2), round((self.y* widthDif) - self.imageSurface.get_height()/2)))

    ## Resize Image
    def resize(self, widthDif):
        self.imageSurface = pygame.Surface((round(self.width * widthDif),round(self.height * widthDif)),pygame.SRCALPHA)
        
        if self.alpha != 255:
            self.imageSurface.set_colorkey((0,0,100))
            self.imageSurface.set_alpha(self.alpha)
        
        self.imageSurface.blit(pygame.transform.scale(self.OriginalImageSurface,(round(self.width * widthDif),round(self.height * widthDif))),(0,0))








## Box
class box:
    def __init__(self, widthDif, x, y, width, height, roundedCorner = 0, colour = (255,255,255), alpha = 255, centered = False, display = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.centered = centered
        self.display = display

        self.colour = colour
        self.alpha = alpha

        self.roundedCorner = roundedCorner

        if self.roundedCorner > 0:
            self.boxSurface = pygame.Surface((round(width* widthDif),round(height * widthDif)),pygame.SRCALPHA)

        else:
            self.boxSurface = pygame.Surface((round(width* widthDif),round(height * widthDif)))

        if alpha < 255:
            self.boxSurface.set_colorkey((0,0,100))
            self.boxSurface.set_alpha(alpha)

        pygame.draw.rect(self.boxSurface,self.colour,(0,0,round(width* widthDif),round(height* widthDif)),border_radius=round(self.roundedCorner* widthDif))


    def draw(self,surf, widthDif):
        if self.display:
            if self.centered == False:
                surf.blit(self.boxSurface, (round(self.x * widthDif), round(self.y * widthDif)))
            
            else:
                surf.blit(self.boxSurface, (round((self.x* widthDif) - self.boxSurface.get_width()/2), round((self.y* widthDif) - self.boxSurface.get_height()/2)))

    def resize(self,widthDif):
        if self.roundedCorner > 0:
            self.boxSurface = pygame.Surface((round(self.width* widthDif),round(self.height * widthDif)),pygame.SRCALPHA)

        else:
            self.boxSurface = pygame.Surface((round(self.width* widthDif),round(self.height * widthDif)))

        self.boxSurface.set_colorkey((0,0,100))
        self.boxSurface.set_alpha(self.alpha)
        pygame.draw.rect(self.boxSurface,self.colour,(0,0,round(self.width* widthDif),round(self.height* widthDif)),border_radius=round(self.roundedCorner* widthDif))







## Entry Box
class entryBox:
    def __init__(self, widthDif, x, y, width, height, font, textColour = (255,255,255),  boxColour = None, alpha = 255, inputTime = 2, centered = False, display = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.centered = centered
        self.display = display
        
        self.boxColour = boxColour
        self.alpha = alpha

        self.entryBoxSurface = createSurface(widthDif, width, height, boxColour, alpha)

        self.font = font
        self.textColour = textColour

        self.text = ""

        self.inputTime = inputTime
        self.timer = 0
        self.input = False
        self.previousInput = None


    ## Draws entryBox surface on another surface
    def draw(self, surf, widthDif):
        if self.display:
            self.entryBoxSurface = createSurface(widthDif, self.width, self.height, self.boxColour, self.alpha) # Creates a background surface

            textSurf = createText(self.text, self.font, self.textColour, round(self.height * widthDif)) # Creates the text
            
            if textSurf.get_width() > self.entryBoxSurface.get_width(): # checks if the text is longer than the entry box
                self.entryBoxSurface.blit(textSurf, (-(textSurf.get_width()-self.entryBoxSurface.get_width()), -24 * round(self.height * widthDif)/100)) # moves text back as more is added
            
            else:
                self.entryBoxSurface.blit(textSurf, (0, -24 * round(self.height * widthDif)/100))

            if self.centered == False:
                surf.blit(self.entryBoxSurface, (round(self.x * widthDif), round(self.y * widthDif))) # Draws entry box not centered
                
            
            else:
                surf.blit(self.entryBoxSurface,(round((self.x - self.width/2) * widthDif), round((self.y - self.height/2) * widthDif))) # Draws entry box centered

    ## Resizes
    def resize(self, widthDif):
        ## Creating new resized menu surface
        self.menuSurface = createSurface(widthDif, self.width, self.height, self.boxColour, self.alpha)


    ## Checks if text needs updating based upon the
    ## inputs from the user. Updates the entry box
    ## and returns an update request for the menu
    ## (Don't ask how it works, a lot of fine tuning
    ## and it still feels like shit so don't change 
    ## it xD)
    def enterText(self, inputList, alphabetList, numberList, otherCharList, dt):
        updateRequest = False

        if self.display:
            if inputList != None:
                if self.previousInput == inputList[0]:
                    
                    if inputList[0] == "backspace":
                        inputTime = self.inputTime*3
                    
                    else:
                        inputTime = self.inputTime*5
                
                else:
                    if inputList[0] == "shift" and len(inputList) > 1:
                        if self.previousInput == inputList[1]:
                            inputTime = self.inputTime*2.5

                        else:
                            inputTime = self.inputTime

                    else:
                        inputTime = self.inputTime


                if self.timer >= inputTime:
                    self.timer = 0
                    self.input = True

                    if inputList[0] in alphabetList or inputList[0] in numberList or inputList[0] in otherCharList:
                        self.text += inputList[0]
                        updateRequest = True

                    elif inputList[0] == "shift":
                        for eachInput in range(len(inputList)-1):
                            if inputList[eachInput+1] in otherCharList:
                                self.text += inputList[eachInput+1]
                                updateRequest = True
                                break
                            
                            elif inputList[eachInput+1] in alphabetList:
                                self.text += inputList[eachInput+1].upper()
                                updateRequest = True
                                break


                    elif inputList[0] == "space":
                        self.text += " "
                        updateRequest = True

                    elif inputList[0] == "backspace":
                        self.text = self.text[:len(self.text)-1]
                        updateRequest = True


                else:
                    self.timer += 1*dt

                if inputList[0] == "shift" and len(inputList) > 1:
                    self.previousInput = inputList[1]
                else:
                    self.previousInput = inputList[0]

            else:
                self.timer = self.inputTime
                self.input = False
                self.previousInput = None

        return updateRequest

    def clear(self):
        self.text = ""







## Menu
class menu:
    def __init__(self, widthDif, x, y, width, height, colour = None, alpha = 255, centered = False, display = True):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.centered = centered
        self.display = display
        self.colour = colour
        self.alpha = alpha

        self.menuSurface = createSurface(widthDif, width, height, colour, alpha)

        self.buttonDic =  {}
        self.textDic = {}
        self.imageDic = {}
        self.boxDic = {}
        self.imageRectDic = {}
        self.entryBoxDic = {}

    ## Draws menu surface on another surface
    def draw(self, surf, widthDif):
        if self.display:
            if self.centered == False:
                surf.blit(self.menuSurface, (round(self.x * widthDif), round(self.y * widthDif)))
            
            else:
                surf.blit(self.menuSurface,(round((self.x - self.width/2) * widthDif), round((self.y - self.height/2) * widthDif)))

    ## Draws all items onto the window
    def drawItems(self,widthDif):
        for eachBox in self.boxDic:
            self.boxDic[eachBox].draw(self.menuSurface, widthDif)

        for eachImage in self.imageDic:
            self.imageDic[eachImage].draw(self.menuSurface, widthDif)

        for eachText in self.textDic:
            self.textDic[eachText].draw(self.menuSurface, widthDif)

        for eachButton in self.buttonDic:
            self.buttonDic[eachButton].draw(self.menuSurface, widthDif)

        for eachEntryBox in self.entryBoxDic:
            self.entryBoxDic[eachEntryBox].draw(self.menuSurface, widthDif)


    ## Resizes menu and all items inside it
    def resize(self, widthDif):
        ## Creating new resized menu surface
        self.menuSurface = createSurface(widthDif, self.width, self.height, self.colour, self.alpha)

        ## Resizes all items in dics
        for eachBox in self.boxDic:
            self.boxDic[eachBox].resize(widthDif)

        for eachImage in self.imageDic:
            self.imageDic[eachImage].resize(widthDif)

        for eachText in self.textDic:
            self.textDic[eachText].resize(widthDif)

        for eachButton in self.buttonDic:
            self.buttonDic[eachButton].resize(widthDif)

        for eachEntryBox in self.entryBoxDic:
            self.entryBoxDic[eachEntryBox].resize(widthDif)

        self.drawItems(widthDif)

    def clearEntryBox(self, widthDif, name):
        self.entryBoxDic[name].clear()
        self.resize(widthDif)






## UI
class UI:
    def __init__(self, winWidth, winHeight, caption, backgroundColour = (0,0,0), icon = None, resizable = True, fullscreen = False, showFPS = False):
        
        ## Setting up window
        if resizable == True and fullscreen == True:
            self.win = pygame.display.set_mode((winWidth,winHeight),pygame.RESIZABLE | pygame.FULLSCREEN)
        
        elif resizable == False and fullscreen == True:
            self.win = pygame.display.set_mode((winWidth,winHeight),pygame.FULLSCREEN)
        
        elif resizable == True and fullscreen == False:
            self.win = pygame.display.set_mode((winWidth,winHeight),pygame.RESIZABLE)
        
        else:
            self.win = pygame.display.set_mode((winWidth,winHeight))

        self.winWidth = winWidth
        self.winHeigth = winHeight
        pygame.display.set_caption(caption) # Sets caption
        self.backgroundColour = backgroundColour # Sets background colour
        self.widthDif = self.win.get_width() / 1920 # Difference between current width and 1920
        
        ## Setting icon
        if icon != None:
            iconImage = pygame.image.load(icon)
            pygame.display.set_icon(iconImage)

        ## Setting up clock, time and FPS
        self.clock = pygame.time.Clock()
        self.lastTime = time.time()
        self.dt = time.time() - self.lastTime
        self.FPS = FPSCounter(self.win,showFPS)

        ## Setup Dictionaries
        self.menuDic = {}

        ## Input Settings
        self.clickCounter = 0
        self.mousePos = pygame.mouse.get_pos()
        self.mousePress  = pygame.mouse.get_pressed()
        self.inputQueue = []

        ## Characters allowed for input
        self.alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numberList = ['1','2','3','4','5','6','7','8','9','0']
        self.otherCharList = ["`","~","!","@","#","$","%","^","&","*","(",")","_","+","-","=","[","]","{","}",";",":","'",'"',",","<",">",".","/","?","\\","|",'£']

        ## Audio settings
        self.audioDic = {}



    ## Update time and FPS
    def updateTime(self, framerate):
        self.clock.tick(framerate)

        self.dt = time.time() - self.lastTime # Checks how much time passed dt = delta time
        self.dt *= 60 # One second passing == 60 frames
        self.lastTime = time.time()

        if self.FPS.displayInWindow or self.FPS.displayInTerminal:
            self.FPS.update(self.win,self.widthDif)

    def updateCursor(self):
        self.mousePos, self.mousePress = pygame.mouse.get_pos(), pygame.mouse.get_pressed()

        if self.mousePress[0] == True:
            self.clickCounter += 1
        
        else:
            self.clickCounter = 0



    ##  ------ UI Audio ------  ##

    ## Sets volume of audio class (0-100)
    def setVolume(self, name, value):
        self.audioDic[name].volume = value

    ## Add audio class to dic
    def addAudio(self, name, filename, volume = 50):
        self.audioDic[name] = loadAudio(filename)
        setVolume(self.audioDic[name], volume)

    ## Returns current state of audio (paused, playing, ...)
    def getState(self, name):
        return getState(self.audioDic[name])

    ## Sets speed of playback
    def setSpeed(self, name, value):
        setSpeed(self.audioDic[name], value)

    ## Returns speed of playback
    def getSpeed(self, name):
        return getSpeed(self.audioDic[name])

    ## Starts audio playback (block - stops thread until playback ends)
    def play(self, name, loop = False, block = False):
        self.audioDic[name].play(loop, block)

    ## Pauses audio playback
    def pause(self, name):
        self.audioDic[name].pause()

    ## Resumes audio playback
    def resume(self, name):
        self.audioDic[name].resume()

    ## Stops audio playback
    def stop(self, name):
        self.audioDic[name].stop()

    ## Closes audio
    def close(self, name):
        self.audioDic[name].close()
    
    ## Moves playback to specified position
    def setPos(self, name, position):
        self.audioDic[name].seek(position)





    ## Add Menu to dic
    def addMenu(self, name, x, y, width, height, colour, alpha = 255, centered = False, display = True):
        self.menuDic[name] = menu(self.widthDif, x, y, width, height, colour, alpha, centered, display)

    ## Add image to menu
    def addImage(self, menuName, name, x, y, imageStr, width = None, height = None, alpha = 255, centered = False, display = True):
        self.menuDic[menuName].imageDic[name] = image(self.widthDif, x, y, imageStr, width, height, alpha, centered, display)

    ## Add box to menu
    def addBox(self, menuName, name, x, y, width, height, roundedCorner = 0, colour = (255,255,255), alpha = 255, centered = False, display = True):
        self.menuDic[menuName].boxDic[name] = box(self.widthDif, x, y, width, height, roundedCorner, colour, alpha, centered, display)

    ## Add button to menu
    def addButton(self, menuName, name, x, y, unpressSurface, pressSurface, hoverSurface = None, unpressSurfaceWidth = None, unpressSurfaceHeight = None, pressSurfaceWidth = None, pressSurfaceHeight = None, hoverSurfaceWidth = None, hoverSurfaceHeight = None, buttonType = "press", press = False, pressAudio = None, hoverAudio = None, pressAudioVolume = 50, hoverAudioVolume = 50,   centered = False, display = True):
        self.menuDic[menuName].buttonDic[name] = button(self.widthDif, x, y, unpressSurface, pressSurface, hoverSurface, unpressSurfaceWidth, unpressSurfaceHeight, pressSurfaceWidth, pressSurfaceHeight, hoverSurfaceWidth, hoverSurfaceHeight, buttonType, press, pressAudio, hoverAudio, pressAudioVolume, hoverAudioVolume, centered, display)

    ## Adds Text to menu
    def addText(self, menuName, name, x, y, textStr, font, colour, size, centered = False, display = True):
        self.menuDic[menuName].textDic[name] = text(self.widthDif, x, y, textStr, font, colour, size, centered, display)

    ## Adds Entry Box to menu
    def addEntryBox(self, menuName,  name, x, y, width, height, font, textColour = (255,255,255),  boxColour = None, alpha = 255, inputTime=2, centered = False, display = True):
        self.menuDic[menuName].entryBoxDic[name] = entryBox(self.widthDif, x, y, width, height, font, textColour,  boxColour, alpha, inputTime, centered, display)

    ## Updates specified menu
    def drawMenu(self, menuName):
        self.menuDic[menuName].drawItems(self.widthDif)

    ## Updates all menus
    def drawAllMenu(self):
        for eachMenu in self.menuDic:
            self.drawMenu(eachMenu)


    ## Resizes window and all menus
    def videoResize(self, keepInRatio = True):
        self.winWidth = self.win.get_width()
        if keepInRatio == True:
            self.winHeight = round((self.win.get_width()/16)*9)
            self.win = pygame.display.set_mode((self.winWidth,self.winHeight),pygame.RESIZABLE)
        else:
            self.winHeigth = self.win.get_height()
        self.widthDif = self.win.get_width() / 1920

        for eachMenu in self.menuDic:
            self.menuDic[eachMenu].resize(self.widthDif)
            self.drawMenu(eachMenu)

    ## Draws background, menus and updates display
    def draw(self):
        self.win.fill(self.backgroundColour)

        for eachMenu in self.menuDic:
            self.menuDic[eachMenu].draw(self.win, self.widthDif)


    ## Recieves inputs
    def getKeyboardInputs(self):
        if len(self.inputQueue) > 0:
            self.inputQueue.pop()

        keyboardEvent = keyboard.get_hotkey_name() # Recieves keyboard input

        if len(keyboardEvent) > 0:
            inputList = keyboardEvent.split('+') # Spits inputs into list
            
            self.inputQueue.append(inputList) # Adds inputs to a queue

    ## Checks if character is in input
    def checkKeyInput(self, character, specifyCaps = False):

        if len(self.inputQueue) > 0:
            if specifyCaps == True:
                if character in self.inputQueue[0]:
                    return True
                else:
                    return False
            
            else:
                inputList = []
                for eachInput in self.inputQueue[0]:
                    inputList.append(eachInput.lower())
                
                if character in inputList:
                    return True
                else:
                    return False
        else:
            return False

    ## Returns all inputs from the front of the queue
    def returnKeyboardInputs(self):
        if len(self.inputQueue) > 0:
            return self.inputQueue[0]

    ## Checks all inputs
    def getInputs(self):
        if pygame.mouse.get_focused():
            self.updateCursor()
            self.getKeyboardInputs()

    def clearEntryBox(self, menuName, entryBoxName):
        self.menuDic[menuName].clearEntryBox(self.widthDif,entryBoxName)

    ## Updates a specific menu
    def updateMenu(self, menuName):
        if self.menuDic[menuName].display == True:
            updateRequest = False

            
            for eachEntryBox in self.menuDic[menuName].entryBoxDic:
                updateRequest = self.menuDic[menuName].entryBoxDic[eachEntryBox].enterText(self.returnKeyboardInputs(),self.alphabetList, self.numberList, self.otherCharList, self.dt)

                if updateRequest == True:
                    break
            
            if updateRequest == False:
                for eachButton in self.menuDic[menuName].buttonDic:

                    updateRequest = self.menuDic[menuName].buttonDic[eachButton].checkPress(self.mousePos, self.mousePress[0], self.clickCounter, self.widthDif, self.menuDic[menuName].centered, self.menuDic[menuName].x, self.menuDic[menuName].y, self.menuDic[menuName].width, self.menuDic[menuName].height)

                    if updateRequest == True:
                        break

            
                
            if updateRequest == True:
                self.menuDic[menuName].resize(self.widthDif)

    ## Updates all menus
    def updateAllMenu(self):
        for eachMenu in self.menuDic:
            self.updateMenu(eachMenu)
    
        

