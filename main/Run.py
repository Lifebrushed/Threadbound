import core.Client as Client
import Settings as Settings
import ui.UI as UI

import os

PlayerClient = Client.Client()
GameDisplay = UI.Display()
Running = True

while Running:



    PlayerClient.Key = PlayerClient.getKey()

    os.system('cls' if os.name == 'nt' else 'clear') 

    action = PlayerClient.ActionList.getCurrentAction(PlayerClient)

    action.Use(PlayerClient)

    GameDisplay.showDisplay()

    

    

    

    