import os
import math

class Cell:
    def __init__(self, x, y) -> None:
        self.X = x
        self.Y = y
        self.Value = ""

class Grid:
    def __init__(self, width, height) -> None:
        self.Cells = []
        self.Width = width
        self.Height = height

        for y in range(height):
            for x in range(width):
                self.Cells.append(Cell(x,y))
    
    def getCell(self, x, y):
        for Cell in self.Cells:
            if Cell.X == x and Cell.Y == y:
                return Cell
        else:
            return Cell(0,0)
        

class DisplayGrid(Grid):
    def __init__(self, width, length) -> None:
        super().__init__(width, length)
    
    def partitionTerminal(self):
        total = os.get_terminal_size().columns
        chunk = math.floor(total / self.Width)
        return chunk

    
    def loadScreen(self):
        chunk = self.partitionTerminal()
        for y in range(self.Height):
            row_str = ""
            for x in range(self.Width):
                cell = self.getCell(x,y)

                value = str(cell.Value)
                
                row_str += value.center(chunk)

            print(row_str)




    
    
class Client:
    def __init__(self) -> None:
        self.Input = ""
        self.Screen = DisplayGrid(5, 30)
        

    def getInput(self):
        try:
            pinput = input("*-+-*")
            pinput = str(pinput.lower().strip())
            return pinput
        except:
             return ""

    

