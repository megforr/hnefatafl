'''
Test notebook to try to use the random data to train an agent to learn how to play

Learning strategy (v0):
1. Train an agent to predict the probability of winning (value function) given the game state (current board layout)
    Pull in data stored in data/ folder
    Prob = probability of defenders winning
    1 - Prob = probability of attackers winning
    Allows you to evalute a which moves have the highest probability of leading to a winning state
    Use TD error v(s(t+1), a) - v(s(t), a) to back propogate through NN for learning (like TD-gammon)
2. Next step use look ahead tree search (alpha,beta) or MCTS to search through tree of variations of game play 
    Need to figure out search depth depending on latency (can start with 2-ply)
'''

import json
import pandas as pd
import os
import glob
import numpy as np
#import tensorflow as tf -> Need to get this working
from sklearn.model_selection import train_test_split


def import_json(file_name):
    """ Import json file and convert to dictionary
        :return: dictionary
    """
    with open(file_name, 'r') as f:
        data = json.load(f)

    data_dict = json.loads(data)

    return data_dict

def convert_dict_to_dataframe(data_dict):
    """ Converts a dictionary to a dataframe
        :return: dataframe
    """
    return pd.DataFrame.from_dict(data_dict)

#####################################################################################
### Step 1: Import files from train location
#####################################################################################
num_files_to_import = 5
train_files = os.listdir(os.path.join(os.getcwd(), 'data'))
for idx, file in enumerate(train_files[0:num_files_to_import]):
    if file.endswith('.json'):
        if idx == 0:
            df = convert_dict_to_dataframe(import_json('data/' + file))
        else:
            tmp = convert_dict_to_dataframe(import_json('data/' + file))
            df = pd.concat([df,tmp])
    else:
        pass

### Single file import
# file_name = 'data/train_data_202205081942.json'
# df = convert_dict_to_dataframe(import_json(file_name))

# print(df.shape)
# print(df.head())

print(df['is_defender_winner'].sum())
print(df['is_done'].sum())

#####################################################################################
### Step 1.5: Transform 1 board state into a print statement that you can see
#####################################################################################

game = 0
turn = 1 
run_dttm = '08-05-2022 19:55:18'
row = df[(df['game_nbr'] == game) & (df['turn_nbr'] == turn) & (df['run_dttm'] == run_dttm)].copy() 
print(row)

def render_board_from_df(row):
    """ Take row from dataframe and render so you can visualize the game board
    """
    board_size = 9
    board_cols = row.columns[4:-1]
    board_pos = row[board_cols].values.flatten()

    # reshape piece_type into 9x9 
    board = board_pos.reshape((board_size, board_size))
    print(board, '\n')

render_board_from_df(row)


#####################################################################################
### Step 2: Start training a neural network on the training data
# Want to be able to predict the probability that defenders will (or 1 - prob, is probability that attackers will win)
# get tensorflow working

# predict the probability of winning - what is the value of a position
# use td error as a back propogation technique (t+1)
#####################################################################################

### Step 2a: Define NN architecture

def nn_model(): 
    """
    """
    return np.nan 



## Step 2b: Data Preprocessing - normalizing inputs and/or one hot encode positions on board

def data_preprocessing(df):
    """ Take input dataframe and output clean data ready for training
        X Features: One hot encode what pieces are in what board positions
        Y Features: Make y = 1.0 only on the move where the defenders won the game
        :returns: cleaned x & y features ready for training 
    """
    
    # Need to convert the y-column to only have 1.0 on the move that won the game for defenders 
    # Everything else is 0
    # To estimate the probability of winning for attackers do (1 - prob_defender_win)
    y_cols = 'is_defender_winner'
    # TODO: Below, in the dataframe there is no part of the dataframe where is_done = True. Need to solve this later. 
    df['is_defender_winner'] = np.where(df['is_done'] == True, 'is_defender_winner', 0.0)
    #print(df['is_defender_winner'].sum())
    y_vals = df[y_cols].values

    
    x_cols = df.columns[4:-1]
    #print(x_cols)
    x_vals = [] 
    x_new_cols = []

    for col in x_cols:
        x_new_cols.append(str(col) + '_1') # king 
        x_new_cols.append(str(col) + '_2') # defender
        x_new_cols.append(str(col) + '_3') # attacker 
    # print(len(x_new_cols))
    # print(x_new_cols)

    # One hot encode the features for a1_1 (king in a1 pos), a1_2 (defender in a1 pos), a1_3 (attacker in a1 pos)
    # If all are 0, then no one in that position
    for idx, row in df.iterrows(): # there will be more efficient ways to do this
        row_data = []
        for col in x_cols: 
            val = row[col]            
            if val == 1: 
                row_data.append(1)
            else: 
                row_data.append(0)
            if val == 2:
                row_data.append(1)
            else:
                row_data.append(0)
            if val == 3:
                row_data.append(1)
            else: 
                row_data.append(0)
            
        x_vals.append(row_data)

    return x_vals, y_vals

print('Input dataframe shape: ', df.shape)
x, y  = data_preprocessing(df)
print('Output x-data shape: ', len(x), len(x[0]))
print('Output y-data shape: ', len(y))


### Step 2c: Split into train/test split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
y_train, y_test = y_train.astype(float), y_test.astype(float)

print('X train shape', len(x_train))
print('Y train shape', len(y_train))

print('X test shape', len(x_test))
print('Y test shape', len(y_test))

print('Train prob of winning: ', y_train.sum())
print('Test prob of winning: ', y_test.sum())





#####################################################################################
### Step 3: Predict on a single unseen state that we understand what the board looks like
#####################################################################################