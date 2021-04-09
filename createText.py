import pygame

## Returns a surface to display text
def createText(text,font,colour,size):
    
    fontFormat = pygame.font.SysFont(font,size)

    message = fontFormat.render(text,True,colour)

    return message

## Creates a text box using arguments and returns it as a surface
def createTextBox(text,font,colour,size,textBoxWidth):
    fontFormat = pygame.font.SysFont(font,size)
    
    textList = text.split(" ")

    for eachWord in range(len(textList)):
        textList[eachWord] += " "
        textList[eachWord] = fontFormat.render(textList[eachWord],True,colour)

    lineLengthPixelCount = 0
    lineRowCount = 0
    for eachWord in textList:
        
        if lineLengthPixelCount + eachWord.get_width() <= textBoxWidth:
            lineLengthPixelCount += eachWord.get_width()
        
        else:
            lineLengthPixelCount = 0
            lineRowCount += 1
            lineLengthPixelCount += eachWord.get_width()


    textBoxSurface = pygame.Surface((textBoxWidth,size*(lineRowCount+2)),pygame.SRCALPHA)

    lineLengthPixelCount = 0
    lineRowCount = 0
    for eachWord in textList:
        
        if lineLengthPixelCount + eachWord.get_width() <= textBoxWidth:
            textBoxSurface.blit(eachWord,(lineLengthPixelCount,size*lineRowCount))
            lineLengthPixelCount += eachWord.get_width()
        
        else:
            lineLengthPixelCount = 0
            lineRowCount += 1
            textBoxSurface.blit(eachWord,(lineLengthPixelCount,size*lineRowCount))
            lineLengthPixelCount += eachWord.get_width()

    return textBoxSurface

        