class Client:
    def __init__(self) -> None:
        self.Input = ""
        self.Screen = None
        

    def getInput(self):
        try:
            pinput = input("*-+-*")
            pinput = str(pinput.lower().strip())
            return pinput
        except:
             return ""

    

