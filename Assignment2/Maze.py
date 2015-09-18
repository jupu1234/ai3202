import heapq

"""
Maze.py
Justin Purtell
Assignment 3
CSCI3202
"""

class Node:
    	#initiliazes a node of the graph
	def __init__(self, x, y, wall, mount):
		self.wall = wall
		self.x = x
        	self.y = y
        	self.parent = None
        	self.h = 0
        	self.tot = 0
		self.cost = 0
		self.mount = mount

class AStar:
	#Initiliazes search parameters
	def __init__(self, height, width):
		self.opened = []
		heapq.heapify(self.opened)
		self.closed = set()
		self.nodes = []
		self.height = height
		self.width = width
	
	#Initilizes maze with wall and mountians on the correct nodes
	def init_maze(self, maze):
		wallcount = 0
		mountcount = 0
		for y in range(len(maze)):
			for x in range(len(maze[0])):
				if maze[y][x] is '2':
					wall = False
				else:
					wall = True
				if maze[y][x] is '1':
					mount = True
				else:
					mount = False
				self.nodes.append(Node(x, y, wall, mount))		
		self.start = self.get_node(0, len(maze)-1)
		self.end = self.get_node(len(maze[0])-1, 0)

	# returns a node from a position based on x and y in a list		
	def get_node(self, x, y):
		return self.nodes[y*self.width + x]
	
	#Manhattan distance heuristic
	def Heur1(self, node):
		return 10*(abs(node.x - self.end.x) + abs(node.y - self.end.y))
	#Best first search heuristic value is scaled by how much of the board is left.
	def Heur2(self, node):
		
		adj_l = self.adj_nodes(node)
		bestcost = float("inf")
		for node in adj_l:
			if node.wall:				
				best = node.cost
				if best < bestcost:
					bestcost = best
		return bestcost*abs(node.x - self.end.x)*abs(node.y - self.end.y)
	#Returns a list of adjacent nodes from a passed node
	def adj_nodes(self, node):
		adj_l = []
		if node.x < self.width-1:
			adj_l.append(self.get_node(node.x + 1, node.y))
		if node.y < self.height-1 and node.x < self.width-1:
			adj_l.append(self.get_node(node.x + 1, node.y + 1))
		if node.y < self.height-1:
			adj_l.append(self.get_node(node.x, node.y + 1))
		if node.y < self.height-1 and node.x > 0:
			adj_l.append(self.get_node(node.x - 1, node.y + 1))
		if node.x > 0:
			adj_l.append(self.get_node(node.x - 1, node.y))
		if node.y > 0 and node.x > 0:
			adj_l.append(self.get_node(node.x - 1, node.y - 1))
		if node.y > 0 and node.wall:
			adj_l.append(self.get_node(node.x, node.y - 1))
		if node.y > 0 and node.x < self.width-1:
			adj_l.append(self.get_node(node.x + 1, node.y - 1))
		return adj_l
	
	#Calculates a path cost based off a heuristic, the movement type and if a mountian or not
	def calc_path(self, adj_node, node, heuro):
		if adj_node.mount:
			if adj_node.x is not node.x and adj_node.y is not node.y:
				adj_node.cost = node.cost + 24
			else:
				adj_node.cost = node.cost + 20
		else:
			if adj_node.x is not node.x and adj_node.y is not node.y:
				adj_node.cost = node.cost + 14
			else:
				adj_node.cost = node.cost + 10
	
		adj_node.parent = node
		if heuro == '1':	
			adj_node.h = self.Heur1(adj_node)
		else:
			adj_node.h = self.Heur2(adj_node)
		adj_node.tot = adj_node.cost + adj_node.h
	
	#Returns a list of x, y coordinates of the path that was taken to reach the goal		
	def path_taken(self):
		visited = 1		
		node = self.end
		print 'End  : %d,%d' % (self.end.x, self.height-1 - self.end.y)	
		while node.parent is not self.start:
			node = node.parent
			visited += 1
			print 'path : %d,%d' % (node.x, self.height - node.y - 1)
		print 'Start: %d,%d' % (self.start.x, self.height - self.start.y - 1)
	
		print 'places visited: %d' % visited

