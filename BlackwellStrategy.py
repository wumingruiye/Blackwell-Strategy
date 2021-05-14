import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random
import nashpy as nash

from tqdm.notebook import tqdm
import matplotlib.colors as mcolors




# Generate a mxn two_player game
m, n = 4, 6
game = np.random.randint(0, 100, size=(m, n, 2))
U1 = np.zeros((m, n))
U2 = np.zeros((m, n))

for i in range(m):
    for j in range(n):
        u = game[i,j]
        U1[i,j] = u[0]
        U2[i,j] = u[1]

# Make sure the game has at least one PURE Nash equilibrium
g = nash.Game(U1, U2)
eqs = g.support_enumeration()
list(eqs)




game_matrix = game

num_players = np.ndim(game_matrix) - 1
largest_payoff = np.amax(np.ndarray.flatten(game_matrix))

print('Number of players: ', num_players)
print('Matrix shape: ', np.shape(game_matrix))
print('Largest payoff: ', largest_payoff)






# Useful Function
def num_actions(player):
    return np.shape(game_matrix)[player]

for i in range(0, num_players):
    print('Player ', str(i), "'s actions number: ", num_actions(i))

assert np.shape(game_matrix)[num_players] == num_players, "length of payoff array doesnt match number of players"

class Player:
    def __init__(self, name, benchmark_action, benchmark_payoff, state="d"):
        self.name = name
        self.benchmark_action = benchmark_action
        self.benchmark_payoff = benchmark_payoff
        self.state = state

    def myfunc(self):
        print("Hello my name is " + self.name)

# Create Players
dictionary_of_players = {}

# Initialize actions
initial_actions =[]
for player in range(num_players):
    initial_actions.append(random.randrange(num_actions(player)))
initial_action_tuple = tuple(initial_actions)

# Create players
for player in range(num_players):
    dictionary_of_players["Player " + str(player+1)] = Player('Player '+str(player+1), initial_action_tuple[player],  game_matrix[initial_action_tuple][player])    
    print(dictionary_of_players["Player " + str(player+1)].name, 'Created')
    print('\t State: ', dictionary_of_players["Player " + str(player+1)].state)
    print('\t Action: ', dictionary_of_players["Player " + str(player+1)].benchmark_action)
    print('\t Payoff: ', dictionary_of_players["Player " + str(player+1)].benchmark_payoff)
    print('\n')
    
    

def get_benchmark_profile():
    profile = []
    for player in range(num_players):
        profile.append(dictionary_of_players["Player " + str(player+1)].benchmark_action)
    return tuple(profile)

def phi(a,b):
    return(max(0, (a-b)/2*(largest_payoff+theta)))

def replace_at_index(tup, index, val):
    return tup[:index] + (val,) + tup[index + 1:]





# this function computes a history of playing the game up to some time.
def run_procedure(num_steps):
    game_history = [initial_action_tuple]
    
    for t in tqdm(range(num_steps)):
        next_actions = []
        for player in range(num_players):
            benchmark_profile = get_benchmark_profile()
            current_player = dictionary_of_players["Player " + str(player+1)]
            
            if current_player.state == 'c':
                if random.random() < epsilon: # experiment with probability epsilon
                    new_action = random.randrange(num_actions(player))
                    #print('new_action', new_action)
                    while  new_action == current_player.benchmark_action:
                        new_action = random.randrange(num_actions(player))
                    new_profile = replace_at_index(benchmark_profile, player, new_action)
                    #print('new_profile', new_profile)
                    if game_matrix[new_profile][player] <= current_player.benchmark_payoff:
                        pass
                    if game_matrix[new_profile][player] > current_player.benchmark_payoff:
                        current_player.state = 'c'
                        current_player.benchmark_payoff = game_matrix[new_profile][player]
                        current_player.benchmark_action = new_action
                else: # Do not experiment
                    if game_matrix[benchmark_profile][player] < current_player.benchmark_payoff:
                        current_player.state = 'w'
                    if game_matrix[benchmark_profile][player] == current_player.benchmark_payoff:
                        current_player.state = 'c'
                    if game_matrix[benchmark_profile][player] > current_player.benchmark_payoff:
                        current_player.state = 'h'
                        
            if current_player.state == 'w':
                if game_matrix[benchmark_profile][player] < current_player.benchmark_payoff:
                    current_player.state = 'd'
                if game_matrix[benchmark_profile][player] == current_player.benchmark_payoff:
                    current_player.state = 'c'
                if game_matrix[benchmark_profile][player] > current_player.benchmark_payoff:
                    current_player.state = 'h'   

            if current_player.state == 'h':
                if game_matrix[benchmark_profile][player] < current_player.benchmark_payoff:
                    current_player.state = 'w'
                if game_matrix[benchmark_profile][player] == current_player.benchmark_payoff:
                    current_player.state = 'c'
                if game_matrix[benchmark_profile][player] > current_player.benchmark_payoff:
                    current_player.state = 'c'
                    current_player.benchmark_payoff = game_matrix[benchmark_profile][player]

            if current_player.state == 'd':
                new_action = random.randrange(num_actions(player))
                #print('new_action', new_action)
                while  new_action == current_player.benchmark_action:
                    new_action = random.randrange(num_actions(player))
                #print('benchmark_profile', benchmark_profile)
                new_profile = replace_at_index(benchmark_profile, player, new_action)
                #print('new_profile', new_profile)
                proba = phi(game_matrix[new_profile][player], game_matrix[benchmark_profile][player])
                if random.random() < proba:
                    current_player.state = 'c'
                    current_player.benchmark_payoff = game_matrix[new_profile][player]
                    current_player.benchmark_action = new_action
                else:
                    current_player.state = 'd'
                    
            next_actions.append(current_player.benchmark_action)
        game_history.append(tuple(next_actions))
    return(game_history)
    
    
    
   
 
 



theta = 0.5
epsilon = 0.001

number_of_game_plays = 1000
history_of_play = run_procedure(number_of_game_plays)
