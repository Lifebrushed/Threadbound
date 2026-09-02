import actions.ActionList as ActionList

class Client:
    def __init__(self):
        self.ActionList = ActionList.ActionList()
        self.Key = ""

    def getKey(self):
        try:
            key = input("-+-").lower().strip()
        except:
            key = ""

        return key