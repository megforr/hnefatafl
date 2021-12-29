# how to  color text in terminal https://www.geeksforgeeks.org/print-colors-python-terminal/

import board
import piece
import numpy as np

def prRed(skk):
    print("\033[91m {}\033[00m".format(skk))

class Hnefatafl:
    '''
    Store hnefatafl game play state
    '''

    def __init__(self):
        self.is_red_turn = True
        self.board = board.Board().reset()
        self.piece = piece.Piece()

    def render(self):
        print('\nCurrent game board:\n', self.board, '\n')

    def translate(self, pos):
        '''
        Translate the provided positions to computer positions
        columns = [a,b,c,d,e,f,g] (left to right)
        rows = [1,2,3,4,5,6,7] (bottom (1) to top (7))
        '''
        try:
            row = int(pos[1])
            col = pos[0].upper()
            if row < 1 or row > 7:
                print(f'{row} is not in range from 1-7.')
                return None
            if col < 'A' or col > 'G':
                print(f'{col} is not in range from a-g.')
                return None
            dict_row = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, 7: 0}
            dict_col = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
            return (dict_row[row], dict_col[col])
        except:
            print(f'{pos} is not in the format [letter, a-g][number, 1-7].')
            return None

    def request_start(self):
        start = input('Choose which piece to move [letter, a-g][number, 1-7]: ')
        if start == None: # TODO: Need to fix this
            print('No position selected. Choose again.')
            self.request_start()
        start = self.translate(start)
        # print(start)
        return start

    def request_to(self):
        to = input('Choose where to move to [letter, a-g][number, 1-7]: ')
        if to == None: # TODO: Need to fix this
            print('No end position selected. Choose again.')
            self.request_to()
        to = self.translate(to)
        return to

    def request_move(self):
        '''
        Ask player for `start` and `to` positions
        :return: position tuple
        '''

        start = self.request_start()
        to = self.request_to()

        return start, to

    def is_updown(self, start, to):
        '''
        Check to see if the move selected is left or right only. No diagonal.
        Either row or column difference has to be equal to 0.

        :param start: starting position
        :param to: ending position
        :return: True if legal rook move, false otherwise
        '''
        row_diff = abs(start[0]-to[0])
        col_diff = abs(start[1]-to[1])

        if row_diff > 0 and row_diff <= 6 and col_diff == 0:
            return True
        elif col_diff > 0 and col_diff <= 6 and row_diff == 0:
            return True
        else:
            return False

    def is_clear_path(self, start, to):
        '''
        Check to see if a piece is in your way
        :return: True if path clear
        '''

        # TODO: Need to finish this - can't focus
        # Need to get all of the pieces (rook, emtpy, etc) into a list and make sure the list is completley empty
        # If not completely empty then need to throw error

        row_diff = abs(start[0]-to[0])
        col_diff = abs(start[1]-to[1])
        path = []

        if row_diff != 0:
            for i in np.arange(min(start[0], to[0]), max(start[0], to[0])):
                piece = self.board[(i, 0)]
                path.append(piece)
            print(path)
        elif col_diff != 0:
            for i in range(col_diff):
                path.append()
        else:
            pass
            #return False

        return True

    def is_legal(self, start, to):
        '''
        Verify the chosen move is legal. If not force to choose new move.
        :param start: Piece to move
        :param to: Piece to move to
        :return: None
        '''

        print(self.board[start])

        # check if selected a movable piece
        if self.board[start] == 0 or self.board[start] == 9:
            print('No piece selected. Please select piece.')
            start = self.request_start()
            self.is_legal(start, to)

        # check if selected a piece that matches the turn
        # TODO: Need to check if red selects red pieces, or white selects white rooks
        if self.is_red_turn and int(self.board[start]) != self.piece.rook:
        #if self.is_red_turn and int(self.board[start]) != 2:
            print('Piece selected is not legal. Select new piece.')
            start = self.request_start()
            self.is_legal(start, to)

        # check if moves like a rook
        if not self.is_updown(start, to):
            print('Illegal move selected. Pieces can only move on vertical and horizontal axis.')
            print('Please select new move.')
            start, to = self.request_move()
            self.is_legal(start, to)

        # check if moves over a piece - check clear path
        if not self.is_clear_path(start, to):
            print('Cannot move piece over other pieces.')
            print('Please select new move.')
            start, to = self.request_move()
            self.is_legal(start, to)

        return True

    def is_pinch(self, start, to):
        # check if start, to ends on either side of pinch to remove from board
        return None

    def move(self, start, to):
        '''
        Moves a piece from `start` to `to`.
        Does nothing if:
            There is no piece at the chosen start position
            If the piece chosen is the wrong color
            If it is an invalid move
        '''

        is_legal = self.is_legal(start, to)
        print(is_legal)

        #if self.is_legal(start, to):
            # update the board
        #    self.board[]

        return None

if __name__ == '__main__':

    prRed('\n--------------------------------------------')
    prRed('Hallo Verden! You are now playing Hnefatafl.')
    prRed('--------------------------------------------')

    game = Hnefatafl()
    game.render()

    for turn in range(1): # do first turn

        if turn % 2 == 0:
            prRed('-- Red Muscovites turn --')
        else:
            print('-- White Swedes turn --')

        start, to = game.request_move()
        game.move(start, to)







        # get move, translate move to computer coordinates
        # check moves are legal
            # is it the right turn? Did you move a piece you were allowed to move?
            # Is the move legal? Did it go off the board or move over another piece?
        # check if move captures another piece
