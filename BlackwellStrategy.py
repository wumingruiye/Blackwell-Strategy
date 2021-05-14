import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
from math import sqrt
import nashpy as nash
import quantecon as qe # for computing the stationary distributions of a markov matrix
from tqdm.notebook import tqdm



expanded_mixed = np.array([[[2,29], [16,7]],
                             [[4,7], [6,13]],
                             [[4,4], [6,6]]])

A = np.array([[2, 16], [4, 6], [4, 6]])
B = np.array([[29, 7], [7, 13], [4, 6]])

game_matrix = expanded_mixed

num_players = np.ndim(game_matrix) - 1
largest_payoff = np.amax(np.ndarray.flatten(game_matrix))

print('Number of players: ', num_players)
print('Matrix shape: ', np.shape(game_matrix))
print('Largest payoff: ', largest_payoff)




# Game's Nash equilibria
game = nash.Game(A, B)
print(game)
eqs = game.support_enumeration()
list(eqs)





# Useful Function
def num_actions(player):
    return np.shape(game_matrix)[player]

for i in range(0, num_players):
    print('Player ', str(i), "'s actions number: ", num_actions(i))

assert np.shape(game_matrix)[num_players] == num_players, "length of payoff array doesnt match number of players"

for i in np.ndarray.flatten(game_matrix):
    assert i >= 0, "not all payoffs are non-negative in your game matrix"

def replace_at_index(tup, index, val):
    return tup[:index] + (val,) + tup[index + 1:]

def regret(player, old_action, alt_action, payoff_diffs, hist_length):
    # payoff_diffs[player, old_action, alt_action] is an array of the difference
    # in utilities player would have gotten in the past by playing alt_action
    # wherever they actually played old_action
    return max(0, sum(payoff_diffs[player][old_action][alt_action]) / hist_length)

def update_payoff_diffs(payoff_diffs, action_tuple):
    # payoff_diffs[player, old_action, alt_action] is an array of the difference
    # in utilities player would have gotten in the past by playing alt_action
    # wherever they actually played old_action
    for player in range(num_players):
        assert isinstance(action_tuple[player], int), "what your action tuple isn't made of integers in update_payoff_diffs??????"
        old_action = action_tuple[player]
        assert old_action in range(num_actions(player)), "what your action tuple contains actions that aren't in range for their players in update_payoff_diffs???????"
        old_payoff = game_matrix[action_tuple][player]
        for alt_action in range(num_actions(player)):
            alt_action_tuple = replace_at_index(action_tuple, player,alt_action)
            alt_payoff = game_matrix[alt_action_tuple][player]
            payoff_diffs[player][old_action][alt_action].append(alt_payoff- old_payoff)

# this function computes the distribution over new actions given a previous
# action and an array of regrets for playing the previous action instead of
# other actions. this array has one entry for every action, and the entry for
# the previous action must be zero.
def prob_next_action(player, last_action, regret_array):
    assert regret_array[last_action] == 0, "your regret isn't zero when it should obviously be"
    normalisation_const = (num_actions(player) - 1) * largest_payoff
    probs_array = [regret / normalisation_const for regret in regret_array]
    prob_last_action = 1 - sum(probs_array)
    probs_array[last_action] = prob_last_action
    return probs_array





# this function computes a history of playing the game up to some time.
# this function computes a history of playing the game up to some time.
def run_procedure(num_steps):
    asyn = [1, 1] # boolean for the state of player 1 and 2. Initially, both players are in ASYN
    state_history = [asyn] # list tracking the transitions from SYN <-> ASYN for both players

    initial_actions = []
    for player in range(num_players):
        initial_actions.append(random.randrange(num_actions(player)))
    initial_action_tuple = tuple(initial_actions)
    initial_action_tuple = (0, 0)

    game_history = [(0, 0)]
    
    max_regret_history = [] # variable to track the evolution of the maximum of the regret for each player
    mixed_strategies = [] # Mixed strategies of each player
    regret_matrices = []
    regret_arrays = []

    # initialise payoff_diffs
    payoff_diffs = [[] for player in range(num_players)]
    for player in range(num_players):
        payoff_diffs[player] = [[] for old_action in range(num_actions(player))]
        for old_action in range(num_actions(player)):
            payoff_diffs[player][old_action] = [[] for alt_action in range(num_actions(player))]
    
    for t in tqdm(range(num_steps)): # Apply regret matching up to 'RM_horizon' to make sure all strategy supports are covered
        #print("###########################", "iteration ", str(t), "####################################")
        next_actions = []
        max_regrets = []
        mxd_stg = []
        rgt_array = []
        hist_length = len(game_history)
        update_payoff_diffs(payoff_diffs, game_history[-1])

        for player in range(num_players): # for each player, compute the mixed strategies using the regret and draw an action
            #print('Player ', str(player+1))
            actions = range(num_actions(player))
            old_action = game_history[-1][player]
            #print('OLD ACTION', old_action)
            regret_array = [regret(player, old_action, alt_action, payoff_diffs, hist_length) for alt_action in actions]
            regret_matrix = [[regret(player, old_action, alt_action, payoff_diffs, hist_length) for alt_action in actions] for old_action in actions]
            max_R = np.amax(regret_matrix)
            max_regrets.append(max_R)

            prob_array_conditional = prob_next_action(player, game_history[-1][player], regret_array)
            rgt_array.append(regret_array)

            ### Probability stochastic matrix
            if player == 1:
                prob_matrix = [[0, 0], [0, 0]]
            else:
                prob_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                
            prob_matrix[old_action] = prob_array_conditional
            #print('\t MATRIX PROBABILITY AFTER FIRST ADD ', prob_matrix)
            
            for alt_action in actions:
                if alt_action != old_action:
                    regret_array = [regret(player, alt_action, act, payoff_diffs, hist_length) for act in actions]
                    prob_array_other = prob_next_action(player, alt_action, regret_array)
                    prob_matrix[alt_action] = prob_array_other
            
            #print('\t MATRIX PROBABILITY IN FINAL', prob_matrix)
            mc = qe.MarkovChain(prob_matrix)
            mc.stationary_distributions
            #print('\t Probability vector (eigenvector)', mc.stationary_distributions[0])
            
            next_actions.append(np.random.choice(num_actions(player), p = mc.stationary_distributions[0]))
            rgt_array.append(regret_array)
            #print('next_actions ', next_actions)

        regret_arrays.append(rgt_array)
        max_regret_history.append(max_regrets)
        game_history.append(tuple(next_actions))
        state_history.append(asyn)
        mixed_strategies.append(mxd_stg)
    return(game_history, state_history, mixed_strategies, regret_arrays, max_regret_history)
    
    
   
 
 



theta = 0.5
epsilon = 0.001

number_of_game_plays = 1000
history_of_play = run_procedure(number_of_game_plays)
