
import numpy as np
import piece
import math

class Board:
    '''
    Store the internal state of the board
    '''
    def __init__(self, board_size=7):
        # initialize a standard 7x7 hnefatafl board
        self.board_size = 7
        #self.board = np.arange(0,board_size**2).reshape(board_size, board_size)
        self.board = np.zeros([self.board_size, self.board_size])

    def reset(self):
        self.board = np.zeros([self.board_size, self.board_size])
        self.board[[0, 0, self.board_size - 1, self.board_size - 1],
                   [0, self.board_size - 1, 0,self.board_size - 1]] = piece.Piece().safe
        self.board[math.floor(self.board_size / 2), math.floor(self.board_size / 2)] = piece.Piece().king

        if self.board_size == 7:
            self.board[0, 2:5] = piece.Piece().rook
            self.board[2, [0, 6]] = piece.Piece().rook
            self.board[3, [0, 6]] = piece.Piece().rook
            self.board[4, [0, 6]] = piece.Piece().rook
            self.board[6, 2:5] = piece.Piece().rook
            self.board[2, 2:5] = piece.Piece().rook
            self.board[3, [2, 4]] = piece.Piece().rook
            self.board[4, 2:5] = piece.Piece().rook
        else:
            pass

        return self.board

    # maybe instead store the locations of each of the red board pieces
    #def red_pieces(self):