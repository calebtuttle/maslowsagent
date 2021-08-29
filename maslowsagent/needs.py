

class Need():
    
    def __init__(self):
        self.name = 'Need'
        self.active = True
        self.location = (0, 0) # location on the board
        self.steps_without = 0
        self.required_after = 10 # need is required after 10 steps
        
    def __repr__(self):
        return self.name[0].upper()
    
    def motivation_factor(self):
        return self.steps_without / self.required_after

