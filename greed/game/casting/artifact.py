from game.casting.actor import Actor

class Artifact(Actor):
    
    def __init__(self):
        super().__init__()
        self.points = 0
    
    def get_points(self):
        if (self.get_text() == '*'):
            self.points = 1
        else:
            self.points = -1
        
        return self.points