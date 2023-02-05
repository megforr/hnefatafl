# <u>Hnefetafl</u> 
* Ancient Viking Chess Board Game
* Starting with  


### Directory
* /game -> classes related to game
  * board
  * piece 
* /agent -> different action selection policies
  * BaseAgent
  * RandomAgent
  * MCTSAgent
* /data -> data collected from different agents game plays
* play.py -> runs the game with the specified agent 

### Inspired by works here: 
* Deep Reinforcement Learning, Hands On - Maxim Lapan
* Meta Ai, CICIERO (Diplomacy) 
  * https://github.com/facebookresearch/diplomacy_cicero
* Game board:
  * https://levelup.gitconnected.com/chess-python-ca4532c7f5a4

### Todo:
* Read about pygame, structuring an OOO game, and making a gym environment
* Can I interact with the game using pygame? 
* Can I create an env similar to a gym environment?
  * env.reset()
  * env.observation_space
  * next_state, reward done, info = evn.step(action)
  * env.action_space.n
  * How do these render? 
* What does pygame do? 
* What was the old code that I used that made the Chess game only not in python
  * The example I found on YouTube
1. Read The book that Steven shared - good code structure 
2. Read gym code to get an idea how to structure
3. Read about pygame and what it offers