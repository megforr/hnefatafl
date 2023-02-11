# <u>Hnefetafl</u> 
* Ancient Viking Chess Board Game

### Directory
* <b>/game</b> 
  * classes related to game play and tracking board state
    * board - board state and game rules
    * piece - piece classes
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
* <b>play.py</b> 
  * main function to run multiple games  

### Inspired by works here: 
* Deep Reinforcement Learning, Hands On - Maxim Lapan
* DeepMind, AlphaGo, AlphaZero, MuZero (Go, Chess, Shogi, Atari)
  * Probably best to just start with AlphaZero since it has a single policy network to create a probability dist over moves
  * https://www.deepmind.com/blog/muzero-mastering-go-chess-shogi-and-atari-without-rules
  * https://arxiv.org/src/1911.08265v1/anc/pseudocode.py
  * https://arxiv.org/abs/1911.08265
  * https://medium.com/applied-data-science/how-to-build-your-own-muzero-in-python-f77d5718061a
* Meta Ai, CICIERO (Diplomacy) 
  * https://github.com/facebookresearch/diplomacy_cicero
* Game board:
  * https://levelup.gitconnected.com/chess-python-ca4532c7f5a4

### Todo:
* Read about pygame 
* Possibly rethink methods similar t0 gym
  * env.reset()
  * env.observation_space
  * next_state, reward, done, info = env.step(action)
  * env.action_space.n
