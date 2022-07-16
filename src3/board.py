import numpy as np
import random
import time
import datetime
import json
import pandas as pd

class Board:

    def __init__(self, board_size):
        """
        9x9
        columns = left to right (a - i)
        rows = bottom to top (1 - 9)
        """
        self.board, self.pieces = self.reset(board_size)

    def reset(self, board_size):
        board = np.zeros([board_size, board_size])

        reset_dict = {1.0: [(4,4)], # king
                      2.0: [(4,2), (4,3), # defenders left
                            (2,4), (3,4), # defenders top
                            (4,5), (4,6), # defenders right
                            (5,4), (6,4)], # defenders bottom
                      3.0: [(0,3), (0,4), (0,5), (4,1), # attackers top
                            (3,0), (4,0), (5,0), (1,4), # attackers left
                            (8,3),(8,4),(8,5),(7,4), # attackers bottom
                            (3,8), (4,8), (5,8), (4,7)], # attackers right
                      4.0: [(0,0), (0,8), (8,0), (8,8)]} # safe spots

        for piece_type, locations in reset_dict.items():
            for loc in locations:
                board[loc] = piece_type

        return board, reset_dict