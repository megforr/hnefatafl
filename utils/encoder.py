#!/usr/bin/env python

import numpy as np

class GameStateEncoder:
    """
    Encode or decode game states
    """
    def __init__(self, board_size):
        self.board_size = board_size
        self.bite_len = 3

    def encode(self, board_state):
        """
        Encodes the game state
        :param board: pass in current board state
        :return: encoded board state
        """
        enc_board = np.nan
        return enc_board

    def decode(self, enc_board):
        """
        Take the encoded board state and output the decoded board state.
        :param enc_board:
        :return: decoded board state
        """
        board_state = np.nan
        return board_state