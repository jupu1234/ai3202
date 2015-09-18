from Maze import *

import heapq

"""
Mazesolve.py
Justin Purtell
Assignment 3
CSCI 3202
"""

maze = []

#Chooses world based on user input
print "Enter World1 or World2"
World = raw_input('Enter world:')

#Chooses heuristic based on user input
print "Enter 1 for Heuristic 1 or Enter 2 for Heuristic 2"
hm = raw_input('Enter value:')

#opens the chosen world
with open(World + ".txt") as f:
    for line in f:
        inner_maze = [elt.strip() for elt in line.split()]
        maze.append(inner_maze)

#initializes the maze
mazesol = AStar(len(maze), len(maze[0]))
mazesol.init_maze(maze)

#searches the maze for a path
heapq.heappush(mazesol.opened, (mazesol.start.tot, mazesol.start))

while len(mazesol.opened):
	f, node = heapq.heappop(mazesol.opened)
	mazesol.closed.add(node)

	if node is mazesol.end:
		mazesol.path_taken()
		print mazesol.end.tot
                break

	adj_nodes = mazesol.adj_nodes(node)
	for adj_node in adj_nodes:
		if adj_node.wall and adj_node not in mazesol.closed:
			if (adj_node.tot, adj_node) in mazesol.opened:
				if adj_node.x is not node.x and adj_node.y is not node.y:				
					if adj_node.mount:
						if adj_node.cost > node.cost + 24:
                           				mazesol.calc_path(adj_node, node, hm)
					else: 
						if adj_node.cost > node.cost + 14:
							mazesol.calc_path(adj_node, node, hm)
				else:
					if adj_node.mount:
						if adj_node.cost > node.cost + 20:
                           				mazesol.calc_path(adj_node, node, hm)
					else: 
						if adj_node.cost > node.cost + 10:
							mazesol.calc_path(adj_node, node, hm)	
			else:
				mazesol.calc_path(adj_node, node, hm)
				heapq.heappush(mazesol.opened, (adj_node.tot, adj_node))
		

