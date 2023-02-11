#!/usr/bin/env python

import math
import numpy as np

class SearchNode:
    """ A node in a search tree.

    A SearchNode represents a state and possible continuations from it. Each child
    represents a possible action, and the expected result from doing so.

    Attributes:
        action: The action from the parent node's perspective. Not important for the
            root node, as the actions that lead to it are in the past.
        player: Which player made this action.
        prior: A prior probability for how likely this action will be selected.
        explore_count: How many times this node was explored.
        total_reward: The sum of rewards of rollouts through this node, from the
            parent node's perspective. The average reward of this node is
            `total_reward / explore_count`
        outcome: The rewards for all players if this is a terminal node or the
            subtree has been proven, otherwise None.
        children: A list of SearchNodes representing the possible actions from this
            node, along with their expected rewards.

    Adapted from https://github.com/deepmind/open_spiel/blob/master/open_spiel/python/algorithms/mcts.py
    """

    def __init__(self, action, player, prior):
        self.action = action
        self.player = player
        self.prior = prior
        self.explore_count = 0
        self.total_reward = 0.0
        self.outcome = None
        self.children = []

    def uct_value(self, parent_explore_count, uct_c):
        """Returns the UCT value of child."""
        if self.outcome is not None:
            return self.outcome[self.player]

        if self.explore_count == 0:
            return float("inf")

        return self.total_reward / self.explore_count + uct_c * math.sqrt(
            math.log(parent_explore_count) / self.explore_count)

    def puct_value(self, parent_explore_count, uct_c):
        """Returns the PUCT value of child.

        Original PUCT algorithm paper:
        "Multi-arm Bandits with Episode Context", (Rosin, 2011)
        Also helpful:
        "Monte Carlo Graph Search for AlphaZero", (Czech et al, 2020)
        """
        if self.outcome is not None:
            return self.outcome[self.player]

        return ((self.explore_count and self.total_reward / self.explore_count) +
                uct_c * self.prior * math.sqrt(parent_explore_count) /
                (self.explore_count + 1))


class MonteCarloTreeSearch:
    """
    Search algorithm using monte carlo roll-outs.
    """
    def __init__(self, uct_c, max_simulations):
        self.uct_c = uct_c
        self.max_simulations = max_simulations






