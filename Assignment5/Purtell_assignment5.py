from MDP import *

"""
MDPpolicy.py
Justin Purtell
Assignment 5
CSCI3202
"""

MDPworld = []

epsilon = raw_input('Enter value for epsilon: ')

with open("World1MDP.txt") as world:
    for line in world:
        inner_world = [elt.strip() for elt in line.split()]
        MDPworld.append(inner_world)

MDPworld.reverse()


mdp = MDPpolicy(len(MDPworld), len(MDPworld[0])) ##initliaze maze parameters
mdp.init_MDP(MDPworld)				 ##initliaze the utility of each state and rewards
mdp.value_iteration(float(epsilon))		 ##value iteration			
mdp.path()					 ##prints the path taken
