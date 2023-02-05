#!/usr/bin/env python

import numpy as np


class BaseAgent:
    """ Base agent used to build more complex agents """
    def __init__(self, team):
        self.team = team        # use team to decide which pieces values to store


class RandomAgent(BaseAgent):
    """ Agent that assumes all moves have equal value and chooses moves randomly. """

    def __init__(self, team):
        super().__init__(team)
        self.agent_type = 'random'

    def calc_action_values(self, move):
        """ Random agents assume every action value == 1.0 (equally likely). """
        q_value = 1.0
        return q_value

    def select_action(self, turn_pieces):
        """ Select action with largest value with ties broken arbitrarily. """

        idx = 0
        idx_move_dict = {}
        move_piece_dict = {}
        move_q_value_dict = {}
        for piece in turn_pieces:
            #print(piece.legal_moves)
            for move in piece.legal_moves:
                idx_move_dict[idx] = move
                move_piece_dict[move] = piece
                q_value = self.calc_action_values(move)
                move_q_value_dict[move] = q_value
                idx += 1

        q_vals = np.array(list(move_q_value_dict.values()))
        #print(q_vals)
        action_idx = np.random.choice(np.flatnonzero(q_vals == q_vals.max()))

        selected_move = idx_move_dict[action_idx]
        selected_piece = move_piece_dict[selected_move]
        #print(action_idx, selected_move, selected_piece)

        return selected_piece, selected_move




