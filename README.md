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
  * Methods to search game trajectories
* <b>/utils</b> 
  * helper functions
* <b>play.py</b> 
  * main function to run multiple games  

### Inspired by works here: 
* Deep Reinforcement Learning, Hands On - Maxim Lapan
* DeepMind, AlphaGo, AlphaZero, MuZero (Go, Chess, Shogi, Atari)
  * https://www.deepmind.com/blog/muzero-mastering-go-chess-shogi-and-atari-without-rules
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
