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
        self.board = board.Board()
        self.is_red_turn = True

    def move(self, start, to):
        '''
        Moves a piece from `start` to `to`.
        Does nothing if:
            There is no piece at the chosen start position
            If the piece chosen is the wrong color
            If it is an invalid move
        '''
        return None

def translate(pos):
    '''
    Translate the provided positions to computer positions
    columns = [a,b,c,d,e,f,g] (left to right)
    rows = [1,2,3,4,5,6,7] (bottom to top)
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
        dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
        return (row-1, dict[col])
    except:
        print(f'{pos} is not in the format [letter, a-g][number, 1-7].')
        return None

if __name__ == '__main__':

    prRed('\n--------------------------------------------')
    prRed('Hallo Verden! You are now playing Hnefatafl.')
    prRed('--------------------------------------------')

    game = Hnefatafl()
    game.board.reset()
    game.board.render()

    for turn in range(2): # do 2 whole turns to starts

        if turn % 2 == 0:
            prRed('-- Red turn --')
        else:
            print('-- White turn --')

        start = input('Choose which piece to move [letter, a-g][number, 1-7]: ')
        start = translate(start)
        print(start)

        to = input('Choose where to move to [letter, a-g][number, 1-7]: ')
        to = translate(to)
        print(to)

        if start == None or to == None:
            continue # moves on to next iteration in the loop

        #game.move() # need to finish tomorrow

