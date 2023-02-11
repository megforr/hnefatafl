# <u>Hnefetafl</u> 
* Ancient Viking Chess Board Game
* Fully observable, perfect information game

### Directory
* <b>/game</b> 
  * classes related to game play and tracking board state
    * [board](https://github.com/megforr/hnefatafl/blob/main/game/board.py) - board state and game rules
    * [piece](https://github.com/megforr/hnefatafl/blob/main/game/piece.py) - piece classes
* <b>/agent</b> 
  * Action selection policies
    * BaseAgent - parent agent class 
    * RandomAgent - Assumes all legal moves have equal value, causing a random selection strategy
* <b>/tree</b> 
  * Tree search methods to traverse game trajectories
* <b>/utils</b>
  * helper functions for the game 
  * game_data -> helper functions related to storing game data
    * ReplayBuffer -> class to store x num game data
  * [encoder](https://github.com/megforr/hnefatafl/blob/main/utils/encoder.py) -> Encode/decode board states 
* <b>play.py</b> 
  * main function to run multiple games  

### Inspired by works here:
* DeepMind, AlphaZero variety
  * https://www.deepmind.com/blog/muzero-mastering-go-chess-shogi-and-atari-without-rules
  * https://arxiv.org/src/1911.08265v1/anc/pseudocode.py
  * https://arxiv.org/abs/1911.08265
  * https://medium.com/applied-data-science/how-to-build-your-own-muzero-in-python-f77d5718061a
* [OpenSpiel package by DeepMind](https://github.com/deepmind/open_spiel)
  * [OpenSpiel AlphaZero Doc](https://github.com/deepmind/open_spiel/blob/master/docs/alpha_zero.md)
    * MCTS gets its prior and value from NN (not random rollouts)
      * [AlphaZero Model Code](https://github.com/deepmind/open_spiel/blob/master/open_spiel/python/algorithms/alpha_zero/model.py)
      * [MCTS Code](https://github.com/deepmind/open_spiel/blob/master/open_spiel/python/examples/mcts.py)
      * [MCTS Code 2](https://github.com/deepmind/open_spiel/blob/master/open_spiel/python/algorithms/mcts.py) 
  * [OpenSpiel MCTS](https://github.com/deepmind/open_spiel/blob/master/open_spiel/algorithms/mcts.cc)
* [Meta Ai, CICIERO (Diplomacy)]((https://github.com/facebookresearch/diplomacy_cicero))
* Game board:
  * https://levelup.gitconnected.com/chess-python-ca4532c7f5a4
* Deep Reinforcement Learning, Hands On - Maxim Lapan

### Components: 
* Game rules - ~DONE
* Actor - generate data via self-play using MCTS and a NN as an evaluator
  * 2 <b>MCTCs</b> objects
  * 1 shared NN <b>EVALUATOR</b>
  * Plays self-play games
* Learner - updates the network based on those games
  * Pulls trajectories into a fixed size FIFO <b>REPLAY_BUFFER</b> via a queue
  * Update step will sample minibatches from replay buffer
  * Saves checkpoint
  * Updates actors models
  * Save stats in json file
* Checkpoints