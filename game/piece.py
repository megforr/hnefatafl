#!/usr/bin/env python

import numpy as np
import math


class Piece:
    def __init__(self, team, location, status='alive'):
        self.team = team         # defenders (aka, white), attackers (aka, red)
        self.location = location
        self.status = status     # alive, dead


class King(Piece):
    """ King-specific piece """
    def __init__(self, team, location, status):
        super().__init__(team, location, status)
        self.piece_nbr = self._get_piece_number()
        self.legal_moves = []

    def _get_piece_number(self):
        """ Number used for rendering on board. King == 1 """
        return 1


class Rook(Piece):
    """ Rook-specific piece """
    def __init__(self, team, location, status):
        super().__init__(team, location, status)
        self.piece_nbr = self._get_piece_number()
        self.legal_moves = []

    def _get_piece_number(self):
        """ Number used for rendering on board. King == 1 """
        if self.team == 'defenders':
            return 2
        elif self.team == 'attackers':
            return 3
        else:
            pass
