#!/usr/bin/env python

import numpy as np

class ReplayBuffer:
    """
    Create a class to store a replay buffer of previous games of x length
    Only store games that ended in a win
    Stores tuple: state, action, reward
    """

    def __init__(self,
                 window_size,
                 ):
        self.window_size = window_size
        self.other_thing = np.nan


