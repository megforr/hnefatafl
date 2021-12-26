blocked_path = 'There is a piece in the path.'
incorrect_path = 'This piece does not move in this pattern.'


def check_updown(board, start, to):
    '''
    Check that there are no pieces along the vertical or horiztonal path
    from 'start' to 'to' both non-inclusive
    '''

class Piece:
    '''
    Store the type of pieces and their valid move types
    '''
    def __init__(self):
        self.none = 0
        self.king = 1
        self.rook = 2
        self.safe = 9

    def is_red(self, turn):
        '''check if the current piece if red or white'''
        if turn % 2 == 0:
            return True
        else:
            return False

    def is_king(self, start):
        '''check if current piece is king or rook'''
        #if start[0]
        return None

    def is_pinch(self, start, to):
        '''
        check if the move captures a piece using a pinch
        '''

    def is_king_capture(self, start, to):
        '''
        check if move captures the king on 4 sides
        '''

    def is_valid_move(self, board, start, end):
        '''check if the move'''


        return None