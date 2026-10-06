import os


import display.DisplayGrid as DisplayGrid
import core.Core as Core
import display.DisplayObject as DisplayObject

Running = True
Client = Core.Client()
if Client:
    Client.Screen = DisplayGrid.DisplayGrid(5,35)

Screen = Client.Screen


while Running == True:
    Client.Input = Client.getInput()


    os.system('cls' if os.name == 'nt' else 'clear')


    if Screen != None:
        Screen.loadScreen()




