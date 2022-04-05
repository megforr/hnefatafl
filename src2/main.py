import numpy as np
import random
import time
import datetime

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




class Hnefatafl:

    def __init__(self, board_size=9):
        self.board = Board(board_size).board
        self.pieces = Board(board_size).pieces
        self.captured_defender_pieces = 0
        self.captured_attacker_pieces = 0
        self.is_attacker_turn = True
        self.possible_moves_dict = {}
        self.memory = []

    def render(self):
        """
        TODO: Make the board more user friendly in the print out
        """
        print('\n----- Current Game Board -----')
        print(self.board, '\n')

    def possible_moves(self):
        """
        Find all the possible move_to moves for each piece on the board
        Returns a dictionary of the board locations and their possible moves
        """
        self.possible_moves_dict = {}

        for piece_type, locations in self.pieces.items():
            if piece_type == 4.: # do not need to find moves of safe spots
                continue
            for move_from in locations:
                self.possible_moves_dict[move_from] = [] # create empty list to store move_to
                for row, line in enumerate(self.board): # line of the board
                    for col, element in enumerate(line): # element in line of board
                        if element == 0: # can only move to a position where there isn't already a piece
                            move_to = (row, col)  # tuple of possible move locations
                            self.possible_moves_dict[move_from].append(move_to)
                        elif piece_type == 1 and element == 4: # if piece is king and location = safe corner
                            move_to = (row, col)  # tuple of possible move locations
                            self.possible_moves_dict[move_from].append(move_to)
                        else:
                            # TODO: Need to remember if we can move pieces into safe spots
                            pass

    def choose_piece(self):
        """
        Figure out 
        TODO: Need to figure out how we'll select pieces that aren't random
        """
        if self.is_attacker_turn:
            print('Attackers turn')
            possible_pieces = self.pieces[3.0].copy()
        else:
            print('Defenders turn')
            possible_pieces = self.pieces[2.0].copy() # must copy or you accidentally append the king location to 2.0
            possible_pieces.append(self.pieces[1.0][0])

        piece = random.sample(possible_pieces, 1) # randomly select pieces
        # print('Selected from: ', possible_pieces)
        # print('Piece selected: ', piece)

        return piece[0]

    def check_legal_moves(self, move_from):
        """
        Filter down the possible moves to only legal moves
        """
        legal_moves_to = self.possible_moves_dict[move_from]
        #print('Possible move to locations: ', legal_moves_to)

        # 1. check if up/down, left/right of start position (row or column has to be same as starting pos)
        for move_to in legal_moves_to:
            if not ((move_from[0] - move_to[0] == 0) or (move_from[1] - move_to[1] == 0)): # if not up/down/left/right then move from list
                legal_moves_to = [x for x in legal_moves_to if x != move_to] # keep all moves except the one eliminated

        #print('Revision 1 - Only N|S|E|W moves: ', legal_moves_to)

        # 2. drop any moves where a piece is obstructing the path (all piece type between point A to point B)
        for move_to in legal_moves_to:
            #print('Testing move_to: ', move_to)
            row_min = min(move_from[0], move_to[0])
            row_max = max(move_from[0], move_to[0])
            col_min = min(move_from[1], move_to[1])
            col_max = max(move_from[1], move_to[1])
            move_trajectory = self.board[row_min:row_max+1, col_min:col_max+1].flatten() # do we need to flatten results
            #print('Move trajectory before sort: ', move_trajectory)
            move_trajectory.sort()
            try:
                if move_trajectory[-2] > 0: # if second largest element in array > 0, then the path isn't clear
                    legal_moves_to = [x for x in legal_moves_to if x != move_to]  # keep all moves except the one eliminated
            except:
                if np.max(move_trajectory) > 0: # if single item array only do a max
                    legal_moves_to = [x for x in legal_moves_to if x != move_to]  # keep all moves except the one eliminated
        #print('Revision 2 - Remaining moves after removing obstructed paths: ', legal_moves_to)

        return legal_moves_to

    def choose_move(self, moves_to):
        """
        Randomly choose a move - will have to update later
        """
        move_to = random.sample(moves_to, 1) # randomly select an endpoint
        return move_to[0]

    def change_turn(self):
        if self.is_attacker_turn:
            self.is_attacker_turn = False
        else:
            self.is_attacker_turn = True

    def update_board(self, move_from, move_to):

        piece_type = self.board[move_from]
        # move_from changes to 0.0
        self.board[move_from] = 0.0
        # move_to changes to the move_from piece type
        self.board[move_to] = piece_type

        # Update piece locations
        self.pieces[piece_type].remove(move_from) # remove move_from location
        self.pieces[piece_type].append(move_to) # add move_to location

    def update_board_after_capture(self, captured_piece_locations):
        """
        Update the board to replace any captured peices with 0 location
        TODO: Should I store the captured pieces somewhere?
        """
        for loc in captured_piece_locations:
            piece_type = self.board[loc]
            print(f'Opponent piece {piece_type} captured at position {loc}.')
            self.board[loc] = 0.0
            self.pieces[piece_type].remove(loc) # remove from being selected
            if self.is_attacker_turn:
                self.captured_defender_pieces += 1
            else:
                self.captured_attacker_pieces += 1

    def check_opponent_capture(self, move_from, move_to):
        """
        Check to see if last move captured an opponent piece
        Note: you cannot commit suicide (where you move into a pinch)
        """
        # check the coordinates that are +1 and +2 in every direction
        locs = []
        for x in np.arange(1,3):
            up = (move_to[0] - x, move_to[1])
            down = (move_to[0] + x, move_to[1])
            left = (move_to[0], move_to[1] - x)
            right = (move_to[0], move_to[1] + x)
            locs.append([up, down, left, right])

        # Store any pieces that are captured
        capture_locs = []
        for x in range(4):  # check all 4 directions from move_to location
            # skip if off the board in the negative direction
            if (locs[0][x][0] < 0 or locs[0][x][1] < 0): # if plus 1 coordinates negative then skip
                continue
            elif (locs[1][x][0] < 0 or locs[1][x][1] < 0): # if plus 2 coordinates negative then skip
                continue
            else:
                pass

            # skip if the piece is off the board in the postive direction (will throw error)
            try:
                plus1 = self.board[locs[0][x]]
                plus2 = self.board[locs[1][x]]
                #print(x, plus1, plus2)
            except:
                continue

            #  TODO: what are other ways to pinch? Against the 4.0 slot?
                # If plus1 is off board - continue
            if self.is_attacker_turn: # piece type = 3.0
                if plus1 == 2.0 and plus2 == 3.0:
                    capture_locs.append(locs[0][x])
            else:
                if plus1 == 3.0 and (plus2 == 1.0 or plus2 == 2.0):
                    capture_locs.append(locs[0][x])

        if len(capture_locs) > 0:
            self.update_board_after_capture(capture_locs)
        else:
            pass


    def check_king_capture(self):
        """
        King can be captured by attackers if it is surrounded on all 4 sides (or against edge)
        """
        king_loc = self.pieces[1.0][0]
        up = (king_loc[0]-1, king_loc[1])
        down = (king_loc[0]+1, king_loc[1])
        left = (king_loc[0], king_loc[1]-1)
        right = (king_loc[0], king_loc[1]+1)

        king_corners = []
        for location in [up, down, left, right]:
            try:
                loc = self.board[location]
            except:
                loc = 3.0 # except here catches when +1 = off the board in the postitive direction (9)
            if (location[0] < 0 or location[1] < 0): # if x,y < 0 then it is an edge
                loc = 3.0
            elif loc == 4.0:
                loc = -1.0
            else:
                pass

            king_corners.append(loc)

        #print('The kings corners', king_corners)

        total = np.sum(king_corners)
        # TODO: Confirm if there are any other ways to capture king
        if total >= 12: # all 4 sides have attackers or an edge
            return True
        else:
            return False

    def check_king_win(self):
        """
        Check to see if the king escaped to a safe spot
        """
        # check corners
        board_corners = []
        for loc in [(0,0), (0,8), (8,0), (8,8)]: # corners of board
            board_corners.append(self.board[loc])

        total = np.sum(board_corners)
        if total < 16:
            return True
        else:
            return False



if __name__ == '__main__':

    MAX_GAMES = 2
    MAX_TURNS = 2000
    RUN_DTTM = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    for game_nbr in range(MAX_GAMES):

        print('Game: ', game_nbr)
        start = time.time()
        is_done = False
        winner = 0.0

        game = Hnefatafl(board_size=9)

        print('\n--------------------------------------------------------------------')
        print('------------------------  Game has started! ------------------------')
        print('--------------------------------------------------------------------')

        #for turn in range(MAX_TURNS):
        turn = 1
        while not is_done:
            print('Current turn: ', turn)
            game.render()
            game.possible_moves() # get all possible moves for turn with pieces on board

            # loop until you find a piece with legal moves
            n_legal_moves = 0
            while n_legal_moves == 0:
                move_from = game.choose_piece() # must be here?
                # TODO: Fix below for king (2.0 possible moves) above you append the 4,4 position to possible moves
                moves_to = game.check_legal_moves(move_from) # all possible locations that can be moved to
                n_legal_moves = len(moves_to)

            move_to = game.choose_move(moves_to) # randomly select where to move piece to
            print('Move piece', game.board[move_from], 'from', move_from, 'to', move_to)
            game.update_board(move_from, move_to)

            if game.is_attacker_turn:
                is_done = game.check_king_capture()
                if is_done:
                    winner = 0.0
                    #game.update_game_outcome(winner)
                    print(f'Congratulations! Attackers have won in {turn} turns!')
            elif turn == MAX_TURNS:
                is_done = True
            else:
                is_done = game.check_king_win()
                if is_done:
                    winner = 1.0
                    #game.update_game_outcome(winner)
                    print(f'Congratulations! Defenders have won in {turn} turns!')

            game.check_opponent_capture(move_from, move_to)
            #game.remember(run_dttm, game_nbr, turn, is_done, winner)
            game.change_turn()
            turn += 1

        game.render()
        print('Time to run: ', round(time.time() - start,4), ' seconds.')
        print('Runtime per turn: ', round((time.time() - start) / MAX_TURNS, 4), ' seconds.')
        print('Captured defender pieces: ', game.captured_defender_pieces)
        print('Captured attacker pieces: ', game.captured_attacker_pieces)

        print('\n--------------------------------------------------------------------')
        print(f'------------------------  End of game: {game_nbr}! ------------------------')
        print('--------------------------------------------------------------------')


#### Notes below:

    # TODO: Store features
        # For each turn store these: Game_nbr, turn nbr, board features (What occupies each location on the board?)
        # At end of each game update the
        # At the end of each game:
            # only keep the game record if it results in a win for a single opponent (or maybe keep draws as a 0.0) ?
            # if one of the opponents win update the win or loss column
    # TODO: Maybe need to output at the end of each run to a file that I can store for a long time. Or else will lose all info each run

    # TODO: Learning strategy
        # How does the agent start to learn from the positions you are in
        # Monte Carlo Tree Search - tree search
        # Value function approximation = Minimax search
        # AlphaGo - MCTS tree search, win prediction, probability of each move to take

    ### TODO: Need to ask Mike about who can land on safe places and can you get captured against walls
    ### Need to think about the learning strategy - read the AlphaGo papers again
    ### AI Hnefetafl engine
        ### TODO: create features for end of each step, each board position (either attackers
        ### Add features to memory batch (?)
        ### At end of game either 1 or 0 if defenders win (or draw)
        ### Attackers want to minimize, defenders want to maximize
        ### Max = Defenders, Min = Attackers

