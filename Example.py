import pygame, random
from sys import exit as sysExit
from ui import UI

class rainbowBackground:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.redUp = random.choice([False,True])
        self.greenUp = random.choice([False,True])
        self.blueUp = random.choice([False,True])
        self.red = random.randint(0,255)
        self.green = random.randint(0,255)
        self.blue = random.randint(0,255)

    def draw(self,win,dt,rainbow = True):
        if rainbow == True:
            try:
                pygame.draw.rect(win,(self.red,self.green,self.blue),(self.x,self.y,self.width,self.height))
                
                if self.redUp == False:
                    if self.red > 0:
                        self.red -= 1 * dt
                    else:
                        self.redUp = True
                else:
                    if self.red < 255:
                        self.red += 1 * dt
                    else:
                        self.redUp = False

                if self.greenUp == False:
                    if self.green > 0:
                        self.green -= 1 * dt
                    else:
                        self.greenUp = True
                else:
                    if self.green < 255:
                        self.green += 1 * dt
                    else:
                        self.greenUp = False

                if self.blueUp == False:
                    if self.blue > 0:
                        self.blue -= 1 * dt
                    else:
                        self.blueUp = True
                else:
                    if self.blue < 255:
                        self.blue += 1 * dt
                    else:
                        self.blueUp = False
            except:
                self.red = random.randint(0,255)
                self.green = random.randint(0,255)
                self.blue = random.randint(0,255)
        else:
            pygame.draw.rect(win,(self.red,self.green,self.blue),(self.x,self.y,self.width,self.height))









##  ------ Main Program ------  ##

roonUI = UI(1600, 900, "Project Roon", (0,0,0), "data/images/logo.png")

pygame.mouse.set_cursor(*pygame.cursors.tri_left)

roonUI.addMenu("serverMenu",0,0,360,1080,(37,37,38),255)
roonUI.addButton("serverMenu","home",35,260,"data/images/home1.png","data/images/home3.png","data/images/home2.png",50,50,45,45,48,48,hoverAudio="button.wav", pressAudio = "press.wav",centered=True,buttonType="press")
roonUI.addButton("serverMenu","settings",100,260,"data/images/settings1.png","data/images/settings3.png","data/images/settings2.png",50,50,45,45,48,48,hoverAudio="button.wav", pressAudio = "press.wav",centered=True,buttonType="press")
roonUI.addButton("serverMenu","exit",165,260,"data/images/x1.png","data/images/x3.png","data/images/x2.png",50,50,45,45,48,48,hoverAudio="button.wav", pressAudio = "press.wav",centered=True,buttonType="press")

roonUI.addMenu("roleMenu",1620,0,300,1080,(37,37,38),255)

roonUI.addMenu("messagingEntry",roonUI.menuDic["serverMenu"].width,0,1920-(roonUI.menuDic["serverMenu"].width + roonUI.menuDic["roleMenu"].width),1080,(30,30,30))
roonUI.addBox("messagingEntry","entryBox",10, roonUI.menuDic["messagingEntry"].height-60, roonUI.menuDic["messagingEntry"].width-10*2, 50, 15, (64,68,75))
roonUI.addEntryBox("messagingEntry","Message Box", 65, roonUI.menuDic["messagingEntry"].height-47, roonUI.menuDic["messagingEntry"].width-40*2, 30, "bahnschrift",boxColour=None,textColour=(0,0,0))
roonUI.addButton("messagingEntry","add",35,roonUI.menuDic["messagingEntry"].height-36,"data/images/plus1.png","data/images/plus3.png","data/images/plus2.png",40,40,35,35,38,38, pressAudio = "press.wav",centered=True,buttonType="press")

roonUI.addMenu("ExitPopup",960,500,600,250,(200,100,100),255,True,display = False)
roonUI.addButton("ExitPopup","yes",80,roonUI.menuDic["ExitPopup"].height-80,"data/images/tick1.png","data/images/tick3.png","data/images/tick2.png",50,50,45,45,48,48,centered=True,buttonType="press")
roonUI.addButton("ExitPopup","no",roonUI.menuDic["ExitPopup"].width-80,roonUI.menuDic["ExitPopup"].height-80,"data/images/x1.png","data/images/x3.png","data/images/x2.png",50,50,45,45,48,48,centered=True,buttonType="press")
roonUI.addText("ExitPopup","Question",roonUI.menuDic["ExitPopup"].width/2,80,"Would you like to exit?","bahnschrift",(255,255,255),40,True)

roonUI.addMenu("settingsTab",1920/2,1080/2,1100,600,(200,100,100),255,True,display = False)
roonUI.addText("settingsTab","title",20,10,"Settings","bahnschrift",(255,255,255),50)
roonUI.addButton("settingsTab","FPS",50,150,"data/images/circle1.png","data/images/tick1.png",None,50,50,48,48,centered=True,buttonType="toggle")
roonUI.addText("settingsTab","FPS",100,122,":  Show FPS","bahnschrift",(0,0,0),40)

roonUI.addButton("settingsTab","rainbow background",50,250,"data/images/circle1.png","data/images/tick1.png",None,50,50,48,48,centered=True,buttonType="toggle",press = True)
roonUI.addText("settingsTab","rainbow background",100,222,":  Logo rainbow background","bahnschrift",(0,0,0),40)

roonUI.addButton("settingsTab","music",50,350,"data/images/circle1.png","data/images/tick1.png",None,50,50,48,48,centered=True,buttonType="toggle",press = True)
roonUI.addText("settingsTab","music",100,322,":  Background Music","bahnschrift",(0,0,0),40)

logoBackground = rainbowBackground(0,0,roonUI.menuDic["serverMenu"].width*roonUI.widthDif,220*roonUI.widthDif)

originalLogo = pygame.image.load("data/images/logo.png")
logo = pygame.transform.scale(originalLogo,(round(180*roonUI.widthDif), round(180*roonUI.widthDif)))

roonUI.drawAllMenu()

roonUI.addAudio("1","jazz.mp3",50)
roonUI.play("1",True)


##  ------ Main Loop ------ ##

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            roonUI.menuDic["ExitPopup"].display = True

        elif event.type == pygame.VIDEORESIZE:
            roonUI.videoResize()
            logoBackground = rainbowBackground(0,0,360*roonUI.widthDif,220*roonUI.widthDif)
            logo = pygame.transform.scale(originalLogo,(round(180*roonUI.widthDif), round(180*roonUI.widthDif)))


    if roonUI.menuDic["ExitPopup"].buttonDic["no"].press == True:
        roonUI.menuDic["ExitPopup"].display = False
    
    elif roonUI.menuDic["ExitPopup"].buttonDic["yes"].press == True:
        run = False

    if roonUI.menuDic["serverMenu"].buttonDic["exit"].press == True:
        roonUI.menuDic["ExitPopup"].display = True
    
    elif roonUI.menuDic["serverMenu"].buttonDic["settings"].press == True and roonUI.clickCounter < 2:
        roonUI.menuDic["settingsTab"].display = not roonUI.menuDic["settingsTab"].display


    if roonUI.menuDic["settingsTab"].buttonDic["FPS"].press == True:
        roonUI.FPS.displayInWindow = True
    
    else:
        roonUI.FPS.displayInWindow = False

    if roonUI.menuDic["settingsTab"].buttonDic["music"].press == True:
        roonUI.audioDic["1"].resume()
    
    else:
        roonUI.audioDic["1"].pause()

    if roonUI.menuDic["ExitPopup"].display == True:
        roonUI.menuDic["settingsTab"].display = False

    if roonUI.checkKeyInput("enter"):
        if roonUI.menuDic["messagingEntry"].entryBoxDic["Message Box"].text != "":
            print(roonUI.menuDic["messagingEntry"].entryBoxDic["Message Box"].text)
            roonUI.clearEntryBox("messagingEntry","Message Box")


    roonUI.updateAllMenu()

    roonUI.getInputs()

    roonUI.draw()

    logoBackground.draw(roonUI.win,roonUI.dt,roonUI.menuDic["settingsTab"].buttonDic["rainbow background"].press)

    roonUI.win.blit(logo,(((360*roonUI.widthDif)/2) - (logo.get_width()/2),(220*roonUI.widthDif)/2 - (logo.get_height()/2)))

    roonUI.updateTime(9999)

    pygame.display.update()