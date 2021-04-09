# Pygame-UI

Files needed to use pygame UI Libary:
  - **ui.py**
  - **createText.py**
  - **FPSMonitor.py**


Extrenal Libaries required:
  - **Pygame**
  - **audioPlayer**
  - **keyboard**

Included in this folder is **example.py** showcasing the libary

Creating UI and drawing surfaces:
  - UI(winWidth, winHeight, caption, backgroundColour, icon, resizable, fullscreen, showFPS) - Initialises a UI class
  - .addMenu(name, x, y, width, height, colour, alpha = 255, centered, display) - Adds a menu surface to the window
  - .addImage(menuName, name, x, y, imageStr, width, height, alpha, centered, display) - Adds a image to a menu surface
  - .addBox(menuName, name, x, y, width, height, roundedCorner, colour, alpha, centered, display) - Adds a box to a menu surface
  - .addButton(menuName, name, x, y, unpressSurface, pressSurface, hoverSurface, unpressSurfaceWidth, unpressSurfaceHeight, pressSurfaceWidth, pressSurfaceHeight, hoverSurfaceWidth, hoverSurfaceHeight, buttonType, press, pressAudio, hoverAudio, pressAudioVolume, hoverAudioVolume,   centered, display) - Adds a button to a menu surface
  - .addText(menuName, name, x, y, textStr, font, colour, size, centered, display) - Adds a text to a menu surface
  - .addEntryBox(menuName,  name, x, y, width, height, font, textColour,  boxColour, alpha, inputTime, centered, display) - Adds an entry box to a menu surface
  - .drawAllMenu() - Draws all menus onto UI (**Needs to be run before the main loop**)

Updates in main loop:
  - .updateAllMenu()
  - .getInputs()
  - .draw()
  - .updateTime(framerate)
  - pygame.display.update()
  - .videoResize() - Only use when window has been resized

Playing Audio:
  - .addAudio(name, filename, volume) - Adds a audio
  - .play(name, loop, break) - Plays audio
  - .pause(name) - Pauses audio
  - .resume(name) - Resume audio
  - .stop(name) - Stop audio
  - .close(name) - Close audio

This wasn't really designed for other people to use I just wanted to share it, so it will proabley be some bugs T_T

Have Fun!
