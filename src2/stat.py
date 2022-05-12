'''
Do some summary statistics about data
'''

import numpy as np
import random
import time
import datetime
import json
import pandas as pd
import os

#df = pd.DataFrame()

directory = 'data'
for idx, filename in enumerate(os.listdir(directory)):
    f = os.path.join(directory, filename)
    print(f)
    if os.path.isfile(f) and f.endswith('.json'):
        if idx == 0:
            data = json.loads(json.load(open(f, 'r')))
            df = pd.DataFrame.from_dict(data, orient='columns')
            print(df.shape)

        else:
            data = json.loads(json.load(open(f, 'r')))
            tmp = pd.DataFrame.from_dict(data, orient='columns')
            df = pd.concat([df, tmp])
            print(df.shape)

# total games
tmp = df.groupby(['run_dttm','game_nbr']).agg(winner=('is_defender_winner','max'),
                                              num_turns=('turn_nbr','max')).reset_index()

print(tmp.head(10))

print(tmp.shape) # 999 games
print(tmp['winner'].sum()) #988 / 999 attackers win
print(np.mean(tmp['num_turns'])) # avg number of turns in random play = 228
