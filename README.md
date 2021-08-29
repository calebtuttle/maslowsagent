# Maslow's Agent
Maslow's Agent simulates an _agent_ pursuing _needs_.

Currently, this simulation is represented as a game played on a 2D board by a single AI. The agent and its needs are placed on the board, and the agent pursues whichever need it is most motivated to pursue.

My goal for this project is that it grows more and more complex, eventually gaining the ability to accurately determine, for a human, whether certain needs are met and to provide behavior recommendations for how to meet those needs.

# Motivation
Inspired by [Maslow's heirarchy of needs](http://psychclassics.yorku.ca/Maslow/motivation.htm), and [Stephen Wolfram's exploration of the computational universe](https://www.wolframscience.com/nks/), I created Maslow's Agent so that I could explore (an incredibly tiny sliver of) the decision-making universe. 

Human decision-making is an impressive information processing activity. Maslow's heirarchy of needs presents a good method of finding the signal in the noise of information an agent might perceive.

The purpose of this simulator is, first, to observe how different _decision making functions_ guide the behavior of an agent and, second, to eventually model ideal decision-making within certain domains (e.g., the domain of diet).

# How Maslow's Agent works
Maslow's Agent is an [_agent_](https://en.wikipedia.org/wiki/Intelligent_agent) that pursues _needs_. The only items in an agent's environment are needs. Each need has a _motivation factor_ between 0 and 1. This motivation factor is a function of time. At each step, the agent pursues the need with the highest motivation factor.

For example, consider the environment which has two needs: sleep and food. At step 0, the motivation factor is 0 for sleep and 0.1 for food, so the agent takes one step toward the food. Perhaps the agent needs sleep once every three steps. At step 1, then, the motivation factor is 0.3 for sleep and 0.2 for food, so the agent takes a step toward sleep.

If the motivating factor for any need reaches 1, the need is considered not met, and the agent dies.

