import random

from maslowsagent.game import Need, Agent, Game


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


agent = Agent()
agent.needs[0].required_after = 17
agent.needs[0].location = (5, 1)
# food = Need()
# food.name = 'Food'
# food.location = (3, 7)
# agent.needs.append(food)
agent_y, agent_x = agent.location
agent.needs = gen_random_needs(10, 6, 14, agent_y, agent_x)

game = Game()
game.set_board(7, 15)
game.agent = agent
game.place_agent_and_needs(agent)

game.run()
