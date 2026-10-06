class Cell:
    def __init__(self, x, y) -> None:
        self.X = x
        self.Y = y
        self.Value = str(str(self.X) + "," + str(self.Y))

class Grid:
    def __init__(self, width, height) -> None:
        self.Cells = []
        self.Width = width
        self.Height = height

        for y in range(height):
            for x in range(width):
                self.Cells.append(Cell(x,y))
    
    def getCell(self, x, y):
        for cell in self.Cells:
            if cell.X == x and cell.Y == y:
                return cell
        return Cell(0,0)