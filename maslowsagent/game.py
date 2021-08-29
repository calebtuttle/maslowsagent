import sys
import time

from maslowsagent.needs import Need
from maslowsagent.agent import Agent

class Game():
    '''
    A Game has a board which is populated by pieces.
    Each piece is either an Agent or a Need. There can 
    be only 1 Agent. When run, the Agent pursues the need
    it is most motivated to pursue.
    '''
    
    def __init__(self):
        self.board = [
            []
        ]
        self.agent = Agent()
        self.is_over = False
    
    def set_board(self, height, width):
        '''
        Generate a board such as:
        board = [
            ['_','_','_','_'],
            ['_','_','_','_'],
            ['_','_','_','_'],
            ['_','_','_','_']
        ]
        '''
        assert height > 0
        assert width > 0
        self.board = [
            ['_' for __ in range(width)] for __ in range(height)
        ]
        return self.board

    def print_board(self):
        for ls in self.board:
            for item in ls:
                print(item, end=' ')
            print()

    def _place_piece(self, piece):
        ''' piece must be either an Agent or Need'''
        y, x = piece.location
        if y > len(self.board) or x > len(self.board[0]):
            print(f'Invalid location for {piece.name}.')
            return
        self.board[y][x] = repr(piece)
    
    def place_agent_and_needs(self, agent):
        assert isinstance(agent, Agent)
        for need in agent.needs:
            self._place_piece(need)
        self._place_piece(agent)

    @staticmethod
    def get_path(y1, x1, y2, x2):
        ''' Get path from (y1, x1) to (y2, x2) as a list of
        (y, x) coordinates.
        '''
        if y1 < y2:
            y_path = list(range(y1 + 1, y2 + 1))
        else:
            y_path = reversed(list(range(y2, y1)))
            
        if x1 < x2:
            x_path = list(range(x1 + 1, x2 + 1))
        else:
            x_path = reversed(list(range(x2, x1)))

        y_path = [(y, x1) for y in y_path]
        x_path = [(y2, x) for x in x_path]
        
        path = y_path + x_path
        return path

    def move(self, piece, y, x):
        ''' Move piece to (y, x) '''
        if not piece.active:
            print('Cannot move inactive piece.')
            return

        # Remove piece
        piece_y, piece_x = piece.location
        self.board[piece_y][piece_x] = '_'
    
        # Place piece
        piece.location = (y, x)
        self.board[y][x] = repr(piece)

    def step(self):
        greatest_need = self.agent.determine_greatest_need()
        need_y, need_x = greatest_need.location
        agent_y, agent_x = self.agent.location

        path = self.get_path(agent_y, agent_x, need_y, need_x)
        y, x = path[0]
        self.move(self.agent, y, x)

        # Check whether agent landed on a space with a need
        active_needs = [n for n in self.agent.needs if n.active]
        for need in active_needs:
            if need.location == (y, x):
                need.active = False
                break
        
        for need in active_needs:
            need.steps_without += 1

    def run(self, stop_after=600):
        '''
        stop_after : int
            The game's longest possible duration (in seconds).
        '''
        finish_time = time.time() + stop_after
        self.print_board()
        time.sleep(0.5)
        while not self.is_over and time.time() < finish_time:
            self.step()
            time.sleep(0.3)
            
            for __ in range(len(self.board)):
                sys.stdout.write("\x1b[1A") # move cursor up one line
                sys.stdout.write("\x1b[2K") # clear to end of line
            self.print_board()

            if not self.agent.is_alive():
                print('Agent died. Game over.')
                self.is_over = True

            active_needs = [n for n in self.agent.needs if n.active]
            if not active_needs:
                print('Agent reached all needs. Game over.')
                self.is_over = True
