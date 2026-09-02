import os
import Settings

class DisplayCell:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.Display = ""

class Display:
    def __init__(self):
        self.DisplayMap = []
        for Y in range(31):
            for X in range(4):
                self.DisplayMap.append(DisplayCell(X,Y))

    def showDisplay(self):
        for Y in range(31):
            print(
                str(self.findCell(0,Y).Display).center(Settings.RightChunk) + 
                str(self.findCell(1,Y).Display).center(Settings.getCenterChunk()) +
                str(self.findCell(2,Y).Display).center(Settings.LeftChunk)
                  )


    def findCell(self, X, Y):
        for Cell in self.DisplayMap:
            if Cell.X == X and Cell.Y == Y:
                return Cell

        return DisplayCell(0,0)


class UI:
    def __init__(self):
        pass

    def updateCells(self, Player):




