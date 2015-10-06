"""
MDP.py
Justin Purtell
Assignment 5
CSCI3202
"""

class Node:
	##inializes Nodes
	def __init__(self, x, y, wall, reward):
		self.x = x
		self.y = y
		self.wall = wall
		self.parent = None
		self.reward = reward
		self.utility = 0


class MDPpolicy:
	
	##initializes maze parameters
	def __init__(self, height, width, gamma = 0.9):
		self.closed = set()
		self.nodes = []
		self.height = height
		self.width = width
		self.gamma = gamma
		self.actions = ['l', 'r', 'u', 'd']
	
	##Initializes an array with initial reward values and 0 utilities
	def init_MDP(self, maze):		
		for y in range(len(maze)):
			for x in range(len(maze[0])):
				wall = False
				if maze[y][x] is '0':
					reward = 0       ##reward for an empty space
				if maze[y][x] is '1':
					reward = -1	 ##reward for a mountian space
				if maze[y][x] is '2':
					wall = True      ##indicates space is a wall
					reward = 0	 ##reward for a wall space	
				if maze[y][x] is '3':
					reward = -2	 ##reward for a space with a snake
				if maze[y][x] is '4':
					reward = 1	 ##reward for a space with a barn
				if x is len(maze[7])-1 and y is len(maze)-1:
					reward = 50	 ##reward for goal state
				
				self.nodes.append(Node(x, y, wall, reward))	##Creates a node in the maze with the above information		
		self.start = self.get_node(0, 0)				##sets the start space
		self.end = self.get_node(len(maze[0])-1, len(maze)-1)		##Sets the end node

	##Returns a node given X and Y coordinates of an associated node from a list
	def get_node(self, x, y):
		return self.nodes[y*self.width + x]
	
	##Calculates the utility achieved for each action given a state
	def transition(self, x, y):
		actionval = []
		for s in range(len(self.actions)):
			##Calulates utility of moving left from current state
			if self.actions[s] is 'l':
				tempval = 0
				if x-1 >= 0:				
					tempval = 0.8*self.get_node(x-1, y).utility
				if y+1 <= self.height-1:
					tempval = 0.1*self.get_node(x, y+1).utility + tempval
				if y-1 >= 0:
					tempval = 0.1*self.get_node(x, y-1).utility + tempval
				actionval.append(tempval)
			##Calulates utility of moving right from current state
			if self.actions[s] is 'r':
				tempval = 0
				if x+1 <= self.width-1:				
					tempval = 0.8*self.get_node(x+1, y).utility
				if y+1 <= self.height-1:
					tempval = 0.1*self.get_node(x, y+1).utility + tempval
				if y-1 >= 0:
					tempval = 0.1*self.get_node(x, y-1).utility + tempval
				actionval.append(tempval)
			##Calulates utility of moving up from current state
			if self.actions[s] is 'u':
				tempval = 0
				if y+1 <= self.height-1:				
					tempval = 0.8*self.get_node(x, y+1).utility
				if x+1 <= self.width-1:
					tempval = 0.1*self.get_node(x+1, y).utility + tempval
				if x-1 >= 0:
					tempval = 0.1*self.get_node(x-1, y).utility + tempval
				actionval.append(tempval)
			##Calulates utility of moving down from current state
			if self.actions[s] is 'd':
				tempval = 0
				if y-1 >= 0:				
					tempval = 0.8*self.get_node(x, y-1).utility
				if x+1 <= self.width-1:
					tempval = 0.1*self.get_node(x+1, y).utility + tempval
				if x-1 >= 0:
					tempval = 0.1*self.get_node(x-1, y).utility + tempval
				actionval.append(tempval)
		
		return actionval
	
	## value iteration algorithim finds the max utility of an action to move to the next state  
	def value_iteration(self, epsilon = 0.5):
		delta = float('Inf')
		gamma = self.gamma	
		while delta > epsilon*(1 - gamma)/gamma:
			for s in reversed(self.nodes):
				if s.wall is False:
					currutility = s.utility
					s.utility = s.reward + gamma*max(self.transition(s.x, s.y))
					delta = abs(currutility - s.utility)

	##Prints the path taken and utilities	
	def path(self):
		self.adj_node(self.start)		
		pathl = []
		node = self.end
		pathl.append(node)
		while node.parent is not self.start:
			node = node.parent
			pathl.append(node)
		pathl.append(self.start)	
		print 'start: (x,y)'
		for s in reversed(pathl):
			print '(%d,%d), utility: %0.2f' % (s.x, s.y, s.utility)

		print 'finish'

	##Finds the best move given a state. Used for printing best actions to take
	def adj_node(self, node):
		adj_l = []
		adj_node = []
		if node.x < self.width-1:
			adj_l.append(self.get_node(node.x + 1, node.y).utility)
			adj_node.append(self.get_node(node.x + 1, node.y))	
		if node.y < self.height-1:
			adj_l.append(self.get_node(node.x, node.y + 1).utility)
			adj_node.append(self.get_node(node.x, node.y + 1))
		if node.x > 0:
			adj_l.append(self.get_node(node.x - 1, node.y).utility)
			adj_node.append(self.get_node(node.x - 1, node.y))
		if node.y > 0:
			adj_l.append(self.get_node(node.x, node.y - 1).utility)
			adj_node.append(self.get_node(node.x, node.y - 1))
		
		if node is not self.end:
			adj_node[adj_l.index(max(adj_l))].parent = node
			self.adj_node(adj_node[adj_l.index(max(adj_l))])
