from maslowsagent.needs import Need

class Agent():
    
    def __init__(self):
        self.name = 'Agent'
        self.active = True
        self.location = (0, 0) # y, x
        sleep = Need()
        sleep.name = 'Sleep'
        sleep.required_after = 15
        self.needs = [sleep]
    
    def __repr__(self):
        return self.name[0].upper()
    
    def add_need(self, need):
        assert isinstance(need, Need)
        need_symbols = [repr(need) for need in self.needs]
        if repr(need) in need_symbols:
            print('Invalid need. Choose a different name.')
            return
        self.needs.append(need)
    
    def step(self):
        for need in self.needs:
            need.steps_without += 1
        # Todo: finish this method
    
    def is_alive(self):
        active_needs = [n for n in self.needs if n.active]
        for need in active_needs:
            if need.steps_without > need.required_after:
                return False
        return True
    
    def determine_greatest_need(self):
        active_needs = [n for n in self.needs if n.active]
        greatest_need = active_needs[0]
        greatest_need_mf = greatest_need.motivation_factor()
        for need in active_needs:
            if need.motivation_factor() > greatest_need_mf:
                greatest_need = need
                greatest_need_mf = need.motivation_factor()
        return greatest_need
    