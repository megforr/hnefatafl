#!/usr/bin/env python

import numpy as np
from game.board import Board
from agents import agent

def prRed(skk):
    print("\033[91m {}\033[00m".format(skk))

def play_game(max_turns, board_size, agent1=np.nan, agent2=np.nan):
    """
    Play a single game between 2 players until a winner is declared.
    agent1: What type of agent is being used for defenders
    agent2: What type of agent is being used for attackers
    winner: Return winner as 0 (defender) or 1 (attackers)
    :return: Game stats
    """

    game_stats = {'board_size': board_size,
                  'agent1': agent1,
                  'agent2': agent2,
                  'winner': np.nan}

    board = Board(board_size=9)
    print('Starting board layout: ')
    board.render()

    for turn_nbr in range(max_turns):
        print('Turn number:', turn_nbr, '|', 'Player: ', board.turn)

        # For each turn
        # 1. get all active pieces for the current turn (board)
        turn_pieces = [piece for piece in board.active_pieces if piece.team == board.turn]
        #print('Turn active piece: ', turn_pieces)

        # 2. Choose the agent depending on the current turn
        # Agent estimates the value for each of the moves (agent) & selects one
        if board.turn == 'defenders':
            piece, move = agent1.select_action(turn_pieces)
        else:
            piece, move = agent2.select_action(turn_pieces)

        # print('Chosen piece:', piece)
        # print('Move from: ', piece.location)
        # print('Move to: ', move)

        # 3. update the board (board) -> move the piece, check for pinches, king capture, team winning
        done = board.update_board(piece, move)
        #board.render()

        #print('Is done:', done)

        if done:
            board.render()
            print(board.turn.upper(), 'have won the game! Go celebrate your victory!')
            if board.turn == 'defenders':
                game_stats['winner'] = 0.0
            else:
                game_stats['winner'] = 1.0

            return game_stats
            #break

        # 4. Change the turn so the other agent can play
        board.change_turn()

    return game_stats


if __name__ == '__main__':

    max_games = 5
    max_turns = 300

    agent1 = agent.RandomAgent(team='defenders')
    agent2 = agent.RandomAgent(team='attackers')

    for game in range(max_games):

        prRed('\n--------------------------------------------')
        prRed('Hallo Verden! You are now playing Hnefatafl.')
        prRed(f'This is game {game+1} of {max_games}.')
        prRed('--------------------------------------------\n')

        game_stats = play_game(max_turns, board_size=9, agent1=agent1, agent2=agent2)
        print(game_stats)


    # 6. later:
    # read papers about training RL agent to know how to store the data in a way that is meaningful
    #   store the game stats in a way that can be extracted later for training & analytics
    #   more sophisticated agents - predict the value of each available piece/legal move for current agent turn
    #       if non-random agents - must assign value to each possible move
    # some kind of tree method to look ahead to predict the best possible next move`

    # later later
    # figure out how to store the game information in a way that is valuable for learning