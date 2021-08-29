

from maslowsagent.needs import Need
from maslowsagent.agent import Agent
from maslowsagent.game import Game, game_utils


agent = Agent()
agent.needs[0].required_after = 17
agent.needs[0].location = (5, 1)
# food = Need()
# food.name = 'Food'
# food.location = (3, 7)
# agent.needs.append(food)
agent_y, agent_x = agent.location
agent.needs = game_utils.gen_random_needs(10, 6, 14, agent_y, agent_x)

game = Game()
game.set_board(7, 15)
game.agent = agent
game.place_agent_and_needs(agent)

game.run()
