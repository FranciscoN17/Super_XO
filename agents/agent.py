class Agent:
    
    def __init__(self, player = "X"):
        
        self.player = player

    def getAction(self, state):
        return -1