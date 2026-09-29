import os

import core.Core as Core

Running = True
Client = Core.Client()

while Running == True:
    os.system('cls' if os.name == 'nt' else 'clear')




    Client.Input = Client.getInput()


