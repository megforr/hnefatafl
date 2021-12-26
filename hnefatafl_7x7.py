from src import board


class Hnefatafl:
    '''
    Store hnefatafl game play state
    '''
    def __init__(self):
        self.board = board.Board()
        self.turn = 0


if __name__ == '__main__':
    print('\n--------------------------------------------')
    print('Hallo Verden! You are now playing Hnefatafl.')
    print('--------------------------------------------')

    game = Hnefatafl()
    game.board.render()
