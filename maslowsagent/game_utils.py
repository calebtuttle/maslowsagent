import random

from maslowsagent.needs import Need

def gen_random_needs(num_needs, max_y, max_x, agent_y, agent_x):
    assert num_needs > 0 and num_needs <= 25
    assert max_y * max_x > num_needs
    symbols = 'BCDEFGHIJKLMNOPQRSTUVWXYZ'
    needs = []
    taken_locations = []
    for i in range(num_needs - 1):
        need = Need()
        need.name = symbols[i]
        location = (random.randint(0, max_y), random.randint(0, max_x))
        while location in taken_locations or location == (agent_y, agent_x):
            location = (random.randint(0, max_y), random.randint(0, max_x))
        need.location = location
        need.required_after = random.randint(18, 65)
        needs.append(need)
    return needs