class Action:
    def __init__(self, key, function):
        self.Key = key
        self.Function = function

    def Use(self, player):
        self.Function(player)
