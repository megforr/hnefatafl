#!/usr/bin/env python

import numpy as np
from . import game.board

class BaseAgent:
    """ Base agent used to build more complex agents """
    def __init__(self, team):
        self.team = team        # use team to decide which pieces values to store


class RandomAgent(BaseAgent):
    """ Agent that assumes all moves have equal value and chooses moves randomly. """

    def __init__(self, team):
        super().__init__(team)
        self.agent_type = 'random'

    def predict_action_values(self, move):
        """ Random agents assume every action value == 1.0 (equally likely).

        :param move: a legal move of an active piece for the current turn
        :return: the action value (q-value)
        """
        q_value = 1.0
        return q_value

    def select_action(self, pieces):
        """ Select action (aka, move) with the largest value with ties broken arbitrarily.
        Random Agent assumes that every action value is the same, so it uniformly samples from all legal moves.

        :param pieces: all the active pieces for the current turn
        :return: selected piece and move
        """

        idx = 0
        idx_move_dict = {}
        move_piece_dict = {}
        move_q_value_dict = {}
        for piece in pieces:
            #print(piece.legal_moves)
            for move in piece.legal_moves:
                idx_move_dict[idx] = move
                move_piece_dict[move] = piece
                q_value = self.predict_action_values(move)
                move_q_value_dict[move] = q_value
                idx += 1

        q_vals = np.array(list(move_q_value_dict.values()))
        #print(q_vals)
        action_idx = np.random.choice(np.flatnonzero(q_vals == q_vals.max()))

        selected_move = idx_move_dict[action_idx]
        selected_piece = move_piece_dict[selected_move]
        #print(action_idx, selected_move, selected_piece)

        return selected_piece, selected_move


class HeuristicAgent(BaseAgent):
    """
    Create an agent that will assign 10 value to actions that result in king escape
    TODO: Later add in value to actions if king could be captured by the move.
    """

    def __init__(self, team):
        super().__init__(team)
        self.agent_type = 'heuristic'

    def predict_action_values(self, move):
        """ Heuristic agent gives value of 10 for actions that result in king escape (or capture, later)

        :param move: evaluate a single move
        :return: estimated action value of move
        """

        # TODO: need to see if we can import board
        if board.is_king_captured(piece):
            q_value = 10.0
        else:
            q_value = 0.0

        return q_value

    def select_action(self, pieces):
        """ Select action (aka, move) with the largest value with ties broken arbitrarily.
        Smart Agent predicts the values from a trained net

        :param pieces: all the active pieces for the current turn
        :return: selected piece and move
        """




