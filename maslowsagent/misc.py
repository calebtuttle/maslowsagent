import sys
import time
import random

from needs import Need





def get_path(x1, y1, x2, y2):
    ''' Get path from (x1, y1) to (x2, y2) as a list of
    (x, y) coordinates.
    '''
    if x1 < x2:
        x_path = list(range(x1 + 1, x2 + 1))
    else:
        x_path = reversed(list(range(x2, x1)))
        
    if y1 < y2:
        y_path = list(range(y1 + 1, y2 + 1))
    else:
        y_path = reversed(list(range(y2, y1)))
        
    x_path = [(x, y1) for x in x_path]
    y_path = [(x2, y) for y in y_path]
    
    path = x_path + y_path
    return path

# Initialize board
board_height = 10
board_width = 30
board = new_board(board_height, board_width)
agent_y, agent_x = agent_location = (0, 4) # (y, x) where origin is top left

sleep_y, sleep_x = sleep_location = (random.randint(1, board_height), random.randint(0, board_width))

board[agent_y][agent_x] = 'A'
board[sleep_y][sleep_x] = 'S'


# Simulate agent reaching sleep
path = get_path(agent_x, agent_y, sleep_x, sleep_y)
print_board(board)
time.sleep(2)
for step in path:
    # Remove 'A'
    board[agent_y][agent_x] = '_'
    
    x = step[0]
    y = step[1]
    
    agent_location = agent_y, agent_x = (y, x)
    
    # Place 'A'
    board[y][x] = 'A'
    
    for __ in range(board_height):
        sys.stdout.write("\x1b[1A") # move cursor up one line
        sys.stdout.write("\x1b[2K") # clear to end of line
    print_board(board)
    # print()
    
    time.sleep(0.50)





    

    