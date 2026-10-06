import os
import math

import core.Grid as Grid
        

class DisplayGrid(Grid.Grid):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)
    
    def partitionTerminal(self):
        total = os.get_terminal_size().columns
        chunk = math.floor(total / self.Width)
        return chunk
    
    def loadEnviorment(self, client):
        pass

    
    def loadScreen(self):
        chunk = self.partitionTerminal()
        for y in range(self.Height):
            row_str = ""
            for x in range(self.Width):
                cell = self.getCell(x,y)

                value = str(cell.Value)
                
                row_str += value.center(chunk)

            print(row_str)