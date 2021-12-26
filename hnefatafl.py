import numpy as np
import math

'''
Game play:
Odd by odd shape board (7x7, 9x9, 11x11, 13x13)
White: Swedes; Starts at center of board around the king/castle
Red: Muscovites; Starts around edge of board
Goal: Red to capture King, White to get King to safe spots (burgs)
Pieces removed from board if 'pinched' - surrounded on top/bottom or left/right by opponent 
    Cannot commit suicide (move into a pinch)

Questions:
    How is the king captured? 
    Can the king move the same as the other pieces? 

TODO: 
1. Create a visual basic board to play & players - kind of 
2. Create way to interact with the board and to alternate who is playing
3. Create standard game rules for red/white 
 
Classes: 

if name == main 
    class = Piece (store internal state of each peice)
    class = Board (store internal state of board) 
    class GamePlay = (store rules of the game) 
'''

class Piece:
    def __init__(self):
        self.none = 0
        self.king = 1
        self.w_rook = 2
        self.r_rook = 3
        self.safe = 4

    def is_red(self, turn):
        if turn % 2 == 0:
            return True
        else:
            return False

class Play:
    def __init__(self):
        self.turn = 0

    def is_valid_move(self, board, piece):


    def alternate(self):
        return self.turn + 1

    def choose_piece(self, board):
        chosen_piece = input('Choose which piece to move? Enter value in format: "(x,y)": ')
        row, col = int(chosen_piece[1]), int(chosen_piece[3])
        try:
            if Piece().is_red(self.turn) and board[row, col] == Piece().r_rook:
                return chosen_piece
            elif not Piece().is_red(self.turn) and board[row, col] == Piece().w_rook:
                return chosen_piece
        except:
            print('Error in coordinates provided.')
            return None

    def choose_move(self, board, chosen_piece):
        move_to = input('Choose where you want to move your piece. Enter value in format: "(x,y)": ')
        row, col = int(move_to[1]), int(move_to[3])
        print(row, col)

        if is_valid_move(board, chosen_piece, )

        try:
            print(board[row, col])
        except:
            print('Error in coordinates provided.')

    def is_valid_move(self, board, chosen_piece, move_to):



class Board:
    def __init__(self, board_size=7):
        self.board_size = board_size

    def render(self): # need to show the current version of the board
       print(self.board)

    def reset(self):
        self.board = np.zeros([self.board_size, self.board_size])
        self.board[[0, 0, self.board_size-1, self.board_size-1], [0, self.board_size-1, 0, self.board_size-1]] = Piece().safe
        self.board[math.floor(self.board_size/2), math.floor(self.board_size/2)] = Piece().king

        if self.board_size == 7:
            self.board[0, 2:5] = Piece().r_rook
            self.board[2, [0, 6]] = Piece().r_rook
            self.board[3, [0, 6]] = Piece().r_rook
            self.board[4, [0, 6]] = Piece().r_rook
            self.board[6, 2:5] = Piece().r_rook
            self.board[2, 2:5] = Piece().w_rook
            self.board[3, [2, 4]] = Piece().w_rook
            self.board[4, 2:5] = Piece().w_rook
        else:
            pass

        return self.board

    def play(self):
        '''
        1. request move
        2. verify move
        3. move piece on board
        '''

        game_play = Play()
        chosen_piece = game_play.choose_piece(self.board)
        chosen_move = game_play.choose_move(self.board, chosen_piece)
        print(chosen_move)
        #game_play.verify_move




if __name__ == '__main__':

    print('--------------------------------')
    print('Welcome to Hnefatafl.')
    print('--------------------------------')
    MAX_MOVES = 10
    board = Board()
    board.reset()
    print('Here is the starting board position: \n')
    board.render()

    print('\nRed Muscovites begin the game.')
    board.play()
