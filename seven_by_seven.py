import numpy as np
import time
import tkinter as tk
from io import StringIO

START_BOARD = [
    "+-------------+",
    "|X| |A|A|A| |X|",
    "| | | | | | | |",
    "|A| |D|D|D| |A|",
    "|A| |D|K|D| |A|",
    "|A| |D|D|D| |A|",
    "| | | | | | | |",
    "|X| |A|A|A| |X|",
    "+-------------+",
]

BOARD_7x7 = [
    "+-------------+",
    "| | | | | | | |",
    "| | | | | | | |",
    "| | | | | | | |",
    "| | | | | | | |",
    "| | | | | | | |",
    "| | | | | | | |",
    "| | | | | | | |",
    "+-------------+",
]

class CreateBoard:

    def __init__(self):


class Piece:


class hnefataflEnv:
    '''
    Viking Chess: Hnefatafl

    Description:
    The goal of the game is to ...

    Observations:
    There are __ discrete states since there are
    * 12 attackers
    * 8 defenders + 1 king
    * 7 x 7 board locations
    * = 7 * 7 * 9 * 12 = 5292 locations
    * = 5 * 5 * 4 * 9 * 12 = 10800 locations

    Future: try creating in Tkinter instead
    '''

    def __init__(self, board_size=7):
        self.desc = np.asarray(BOARD_7x7, dtype="c")
        self.board_size = 7


    def reset(self):
        ''' Reset game board to start state '''

    def render(self, mode='human'):
        ''' Create this ready to render the game play '''
        outfile = StringIO() if mode == "ansi" else sys.stdout

        out = self.desc.copy().tolist()
        out = [[c.decode("utf-8") for c in line] for line in out]

        # taxi_row, taxi_col, pass_idx, dest_idx = self.decode(self.s) # would need to create a decode for state



class hnefataflAgent:

    def __init__(self, gamma=0.9, alpha=0.1):
        self.epsilon = 1.0 # epsilon greedy learning
        self.epsilon_decay_rate = 0.5 # how much you decay learning per episodes
        self.epsilon_min = 0.1 # min amount of exploration you do

        self.gamma = 0.9 # how much you care about immediate vs future rewards
        self.alpha = 0.1 # learning rate in nn

    def experience_replay(self):
        ''' create an experience replay buffer to learn from '''


if __name__ == '__main__':
    env = hnefataflEnv()
    env.root.mainloop()
    #self.root.mainloop()


