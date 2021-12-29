'''
Start with 7x7 gameplay
'''


import numpy as np


class Piece:
    def __init__(self):
        self.red_turn = True
        self.none = 0
        self.rook = 1
        self.king = 2

    def alternate(self, turn):
        if turn % 2 == 0:
            self.red_turn = True
        else:
            self.red_turn = False

    # def piece_location(self):
    #     '''
    #     Store the location of each of the pieces on the board
    #     '''




class Board:
    def __init__(self, board_size=7):
        self.board_size = board_size
        self.board = np.arange(0,board_size**2).reshape(board_size, board_size)
        self.red_pieces = []
        self.white_pieces = []

    def render(self):
        '''
        Maybe print a friendly version of the board
        '''
        print(self.board)

    def reset(self):
        '''
        Reset the game to start from new
        '''
        self.board = np.arange(0, board_size ** 2).reshape(board_size, board_size)

        


        return red_pieces, white_pieces





if __name__ == '__main__':

    print('--------------------------------')
    print('Welcome to Hnefatafl.')
    print('--------------------------------')

    board = Board()
    board.render()
    #board.reset()
