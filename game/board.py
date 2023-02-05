#!/usr/bin/env python

import numpy as np
from . import piece


class Board:
    def __init__(self, board_size=9):
        self.board_size = board_size
        self.active_pieces = self.reset_active_pieces()
        self.board_state = self.reset_board()
        self.reset_legal_moves()
        self.turn = 'defenders'  #white starts the game

    def reset_active_pieces(self):
        """ Reset all possible pieces from the game """

        if self.board_size == 9:
            piece_locations = {'white king': [(4, 4)],
                               'white rook': [(2, 4), (3, 4),
                                            (4, 2), (4, 3), (4, 5), (4, 6),
                                            (5, 4), (6, 4)],
                               'red rook': [(3, 0), (4, 0), (5, 0), (4, 1),
                                          (0, 3), (0, 4), (0, 5), (1, 4),
                                          (3, 8), (4, 8), (5, 8), (4, 7),
                                          (8, 3), (8, 4), (8, 5), (7, 4)]}
        else:
            piece_locations = {}

        active_pieces = []
        for key, loc_list in piece_locations.items():
            for loc in loc_list:
                if key == 'white king':
                    active_pieces.append(piece.King(team='defenders', location=loc, status='alive'))
                elif key == 'white rook':
                    active_pieces.append(piece.Rook(team='defenders', location=loc, status='alive'))
                else:
                    active_pieces.append(piece.Rook(team='attackers', location=loc, status='alive'))

        return active_pieces

    def reset_board(self):
        """ Set board back to starting positions """

        board_state = np.zeros((self.board_size, self.board_size))

        # add safe spots (9) in corner
        for safe_spot in [(0, 0),
                          (0, self.board_size - 1),
                          (self.board_size - 1, 0),
                          (self.board_size - 1, self.board_size - 1)]:
            board_state[safe_spot] = 9

        # add game pieces
        for ap in self.active_pieces:
            board_state[ap.location] = ap.piece_nbr

        return board_state

    def render(self):
        """ print board to command line for visualization purposes """
        print(self.board_state, '\n')

    def get_legal_moves(self, piece):
        """ Using the current location get a list of legal moves [(row, col), (row,col)] """
        """ returns a list of legal moves """

        #print('Current piece location: ', piece.location, ' and type ', piece.piece_nbr)

        all_moves = []
        if piece.status == 'dead':
            return all_moves
        else:
            pos_rows = np.arange(0, self.board_size).tolist()
            pos_rows.remove(piece.location[0])
            for r in pos_rows:
                all_moves.append((r, piece.location[1]))

            pos_cols = np.arange(0, self.board_size).tolist()
            pos_cols.remove(piece.location[1])
            for c in pos_cols:
                all_moves.append((piece.location[0], c))

            # from all the moves only keep the ones that are available (not occupied)
            avail_moves = []
            for move in all_moves:
                #print(move, self.board_state[move])
                # if king and safe spot then keep move
                if (piece.piece_nbr == 1) & (self.board_state[move] == 9):
                    avail_moves.append(move)
                # if location is unoccupied then keep move
                elif self.board_state[move] == 0:
                    avail_moves.append(move)
                else:
                    pass
            # print('All moves', piece.location, all_moves)
            # print('Avail moves', piece.location, avail_moves)

            # starting at the piece location itself look N,S,E,W and exclude locations that are on the other side
            N, S, E, W = [],[],[],[]
            for move in avail_moves:
                if move[0] < piece.location[0]:
                    N.append(move)
                elif move[0] > piece.location[0]:
                    S.append(move)
                else:
                    pass

            for move in avail_moves:
                if move[1] > piece.location[1]:
                    E.append(move)
                elif move[1] < piece.location[1]:
                    W.append(move)
                else:
                    pass

            # Look N,S,E,W and remove locations that require you to hop over other pieces
            final_moves = []
            #print('East', E)
            for idx, move in enumerate(E):
                avg_steps = (move[1] - piece.location[1]) / (idx + 1)
                if avg_steps == 1:
                    final_moves.append(move)
                else:
                    pass
            #print(final_moves)

            W.reverse()
            #print('West', W)
            for idx, move in enumerate(W):
                avg_steps = (move[1] - piece.location[1]) / (idx + 1)
                if avg_steps == -1:
                    final_moves.append(move)
                else:
                    pass
            #print(final_moves)

            #print('South', S)
            for idx, move in enumerate(S):
                avg_steps = (move[0] - piece.location[0]) / (idx + 1)
                if avg_steps == 1:
                    final_moves.append(move)
                else:
                    pass
            #print(final_moves)

            N.reverse()
            #print('North', N)
            for idx, move in enumerate(N):
                # print('move', move[0])
                # print('piece loc', piece.location[0])
                # print('idx+1', idx + 1)
                avg_steps = (move[0] - piece.location[0]) / (idx + 1)
                if avg_steps == -1:
                    final_moves.append(move)
                else:
                    pass
                #print(avg_steps)
            #print('Final moves', piece.location, final_moves)

            return final_moves

    def reset_legal_moves(self):
        """ Upon init reset the legal moves by each piece """

        for ap in self.active_pieces:
            ap.legal_moves = self.get_legal_moves(ap)

    def update_board(self, selected_piece, move_to):
        """ Given a selected piece and a move to location, update the board.
            Standard rooks cannot move into safety zones. (TODO: Verify that is not being allowed today).
            Check to see if King made it to safety or was captured.
            :return: done = if game is over due to king escape or capture by opponent
        """

        done = False
        #print('Previous location: ', selected_piece.location)
        #print('New location: ', move_to)

        for piece in self.active_pieces:
            if selected_piece == piece:
                self.board_state[move_to] = piece.piece_nbr        # move the piece to the new location
                self.board_state[piece.location] = 0.              # set the old location to empty
                piece.location = move_to                           # update the stored location in the piece class

                # Check if move causes an opponent piece to be captured - this is called a pinch
                # If yes, update piece to be dead and remove from board
                self.is_opponent_piece_captured(piece)

                # Check if move captured the king (must be pinched on all sides)
                # Or Check to see if the piece that was the moved was the king, and it escaped to safety.
                if piece.team == 'attackers':
                    done = self.is_king_captured(piece)
                elif (piece.team == 'defenders') & (piece.piece_nbr == 1.0):
                    done = self.check_for_king_escape(piece)
                else:
                    pass

            else:
                pass

        # before returning the loop - reset the legal moves
        self.reset_legal_moves()

        return done

    def is_opponent_piece_captured(self, piece):
        """ Check to see the selected piece's move (new location) causes an opponents piece to be captured.
            In hnefatafl this is also referred to as a pinch.
            Check N,S,E,W and see if an opponent piece is next to it with its own player one spot beyond
        """
        #print('piece location: ', piece.location)
        captured_pieces = []

        n = np.arange(0, piece.location[0]+1).tolist()
        n.reverse()
        n = n[:3]
        n = [(nx, piece.location[1]) for nx in n]
        #print('North:', N)
        piece_seq = [self.board_state[loc] for loc in n]
        is_capture, capture_piece_nbr = self.check_piece_sequence_for_capture(piece_seq)
        if is_capture:
            capture_piece_loc = n[1] # TODO: Verify if this is right - is selecting this index correct
            #print(capture_piece_loc)
        else:
            capture_piece_loc = np.nan
        captured_pieces.append(('N', is_capture, capture_piece_nbr, capture_piece_loc))
        #print(is_capture, capture_piece_nbr, capture_piece_loc)

        s = np.arange(piece.location[0], self.board_size).tolist()
        s = s[:3]
        s = [(sx, piece.location[1]) for sx in s]
        #print('South:', S)
        piece_seq = [self.board_state[loc] for loc in s]
        is_capture, capture_piece_nbr = self.check_piece_sequence_for_capture(piece_seq)
        if is_capture:
            capture_piece_loc = s[1]
            #print(capture_piece_loc)
        else:
            capture_piece_loc = np.nan
        captured_pieces.append(('S', is_capture, capture_piece_nbr, capture_piece_loc))
        #print(is_capture, capture_piece_loc)

        e = np.arange(0, piece.location[1] + 1).tolist()
        e.reverse()
        e = e[:3]
        e = [(piece.location[0], ex) for ex in e]
        #print('East:', E)
        piece_seq = [self.board_state[loc] for loc in e]
        is_capture, capture_piece_nbr = self.check_piece_sequence_for_capture(piece_seq)
        if is_capture:
            capture_piece_loc = e[1]
            #print(capture_piece_loc)
        else:
            capture_piece_loc = np.nan
        captured_pieces.append(('E', is_capture, capture_piece_nbr, capture_piece_loc))
        #print(is_capture, capture_piece_loc)

        w = np.arange(piece.location[1], self.board_size).tolist()
        w = w[:3]
        w = [(piece.location[0], wx) for wx in w]
        #print('West:', W)
        piece_seq = [self.board_state[loc] for loc in w]
        is_capture, capture_piece_nbr = self.check_piece_sequence_for_capture(piece_seq)
        if is_capture:
            capture_piece_loc = w[1]
            #print(capture_piece_loc)
        else:
            capture_piece_loc = np.nan
        captured_pieces.append(('W', is_capture, capture_piece_nbr, capture_piece_loc))
        #print(is_capture, capture_piece_loc)

        #print(captured_pieces)
        captured_pieces = [x for x in captured_pieces if x[1] == True]  # keep piece if is_capture == True
        captured_pieces = [x for x in captured_pieces if x[2] != 1.0]  # keep piece only if not king
        captured_pieces = [x[3] for x in captured_pieces] # only keep the location
        #print('Captured pieces: ', captured_pieces)

        if len(captured_pieces) >= 1:
            print('Pieces captured at locations: ', captured_pieces)
            self.set_piece_status_to_dead(captured_pieces)
            self.remove_dead_pieces_from_active_list()
        else:
            pass

    def check_piece_sequence_for_capture(self, piece_seq):
        """ Look for a pinch by seeing the same piece on first and last sequence
            A pinch looks like [attacker, defender, attacker] or [defender, attacker, defender]
            TODO: Eventually try to make this code better. Too hardcoded and gross
        """
        #print(piece_seq)

        team_seq = []
        for piece_nbr in piece_seq:
            if piece_nbr in [1.0, 2.0]:
                team_seq.append('defenders')
            elif piece_nbr in [3.0]:
                team_seq.append('attackers')
            else:
                team_seq.append('empty')
        #print(team_seq)

        is_capture = False
        capture_piece_nbr = np.nan
        if (team_seq == ['attackers', 'defenders', 'attackers']) & (piece_seq.count(1.0) == 1):
            # if attackers surround defenders and king is not the defender
            is_capture = True
            capture_piece_nbr = piece_seq[1]
        elif team_seq == ['defenders', 'attackers', 'defenders']:
            is_capture = True
            capture_piece_nbr = piece_seq[1]
        else:
            pass

        return is_capture, capture_piece_nbr

    def set_piece_status_to_dead(self, captured_pieces): # todo: in the future force this captured pieces to be a list
        """ Loop through captured pieces and set their status = dead. """

        for cap_piece_loc in captured_pieces:
            for act_piece in self.active_pieces:
                if cap_piece_loc == act_piece.location:
                    act_piece.status = 'dead'
                    self.board_state[act_piece.location] = 0. # remove the piece from the board

    def remove_dead_pieces_from_active_list(self):
        """ Iterate through active piece list and remove any pieces that status are now dead. """

        self.active_pieces = [piece for piece in self.active_pieces if piece.status != 'dead']

    def is_king_captured(self, piece):
        """ Check to see if the move caused the King to be captured.
            # TODO: Check the game rules to see in what situations a king is captured
            # TODO: Can a king be captured if it is against a wall and surrounded by 3 opponent pieces? Confirm
        """
        done = False

        # get the kings current location
        king_loc = np.nan
        for ap in self.active_pieces:
            if ap.piece_nbr == 1: # if king
                king_loc = ap.location
        #print('King loc: ', king_loc)

        # look N,S,E,W by a single index. Store the locs & pieces in those locations.
        # If out of bounds take the max of 0 or min of board_size-1
        n_loc = (np.max([0, king_loc[0]-1]), king_loc[1])
        s_loc = (np.min([king_loc[0]+1, self.board_size-1]), king_loc[1])
        e_loc = (king_loc[0], np.min([king_loc[1]+1, self.board_size-1]))
        w_loc = (king_loc[0], np.max([0, king_loc[1]-1]))
        surrounding_locations = [n_loc, s_loc, e_loc, w_loc]
        #print('N', n_loc, '\nS', s_loc, '\nE', e_loc, '\nW', w_loc)

        # pieces around king should add up to 12 (opponents pieces == 3)
        surrounding_piece_val = 0
        for loc in surrounding_locations:
            surrounding_piece_val += self.board_state[loc]

        # if king is surrounded by attackers pieces on all 4 sides
        # AND the piece that was moved is in the list then the king is captured
        if (surrounding_piece_val == 12) & (surrounding_locations.count(piece.location) == 1):
            print('****** The King has been captured! ******')
            done = True
            return done
        else:
            return done

    def check_for_king_escape(self, piece):
        """ Check to see if the king made it to a safe zone.
            If the king makes it to a safe zone, the game is over and defenders win.
        """
        done = False

        safe_locs = [(0, 0),
                      (0, self.board_size - 1),
                      (self.board_size - 1, 0),
                      (self.board_size - 1, self.board_size - 1)]

        # if kings current location is in one of the safe zones then the game is over
        # defenders win
        if safe_locs.count(piece.location) == 1:
            print('****** The King made it to safety! ******')
            done = True
            return done
        else:
            pass

        return done

    def change_turn(self):
        if self.turn == 'attackers':
            self.turn = 'defenders'
        else:
            self.turn = 'attackers'


