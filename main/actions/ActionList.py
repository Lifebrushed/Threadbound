import actions.Action as Action

def Test(player):
    print("dih")

def Fallback(player):
    print("No action")

class ActionList:
    def __init__(self):
        self.List = self.getCurrentList

    def getCurrentList(self):
        return [
            Action.Action("f", Test)
        ]

    def getCurrentAction(self, player):
        key = player.Key

        for action in self.getCurrentList():
            if action.Key == key:
                return action

        return Action.Action("", Fallback)

