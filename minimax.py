#https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/

import math

def minimax(current_depth, node_idx, max_turn, scores, target_depth):
    '''
    In this example - only 2 choices; If more than 2, need to recur for all possible moves
    :param current_depth:
    :param node_idx:
    :param max_turn: Boolean for is this the maximizer's turn
    :param scores:
    :param target_depth:
    :return:
    '''

    # base case: target depth reached
    if current_depth == target_depth:
        return scores[node_idx]

    if max_turn:
        return max(minimax(current_depth+1, node_idx*2, False, scores, target_depth),
                   minimax(current_depth+1, node_idx*2+1, False, scores, target_depth))

    else:
        return min(minimax(current_depth+1, node_idx*2, True, scores, target_depth),
                   minimax(current_depth+1, node_idx*2+1, True, scores, target_depth))


scores = [3,5,2,9,12,5,23,23] # normally we need to derive these values - these are the values at the leaf node
print('Scores: ', scores)

tree_depth = math.log(len(scores), 2)
print('Tree depth: ', tree_depth)

print('The optimal value is: ', end='')
print(minimax(0,0,True, scores,tree_depth))