class HMMfunc:
	#Opens data file and reads it into a list and initializes the dictionaries and the states
	def __init__(self, infile):
		self.Model =[]				
		with open(infile) as manifesto:
    			for line in manifesto:
        			char = [elt.strip() for elt in line.split()]
        			self.Model.append(char)

		self.statespace = []
		self.statespace.append('_')
		for i in range(97, 123):
			self.statespace.append(chr(i))
		self.marg = {}
		self.trans = {}
		self.emis = {}

	#calculates each time a letter is seen and the time it is typed wrong and the number of times the next letter will be seen with the current letter
	#using dictionaries
	def calcocc(self):
		for i in range(0, len(self.Model)-1):
			state1 = self.Model[i][0]
			state2 = self.Model[i+1][0]
			emission = self.Model[i][1]
	
			if self.marg.has_key(state1):
				self.marg[state1] += 1
			else:
				self.marg[state1] = 1

			if self.trans.has_key(state1):
				if self.trans[state1].has_key(state2):
					self.trans[state1][state2] += 1
				else:
					self.trans[state1][state2] = 1
			else:
				self.trans[state1] = {state2:1}

			if self.emis.has_key(state1):
				if self.emis[state1].has_key(emission):
					self.emis[state1][emission] += 1
				else:
					self.emis[state1][emission] = 1
			else:
				self.emis[state1] = {emission:1}
	#Fills missing states into dictionaries and calculates probabilites with the soomthing equation and then prints the probabilities into Assignment8out.txt
	def printdata(self):
		for i in self.statespace:	
			for j in self.statespace:
				if self.trans.has_key(i):
					if not self.trans[i].has_key(j):	
						self.trans[i][j] = 0
		for i in self.statespace:	
			for j in self.statespace:
				if self.emis.has_key(i):
					if not self.emis[i].has_key(j):	
						self.emis[i][j] = 0
		with open("Assignment8out.txt", "w") as text_file:
			text_file.write("Marginal probabilities:\n")
			text_file.write("\n")
			for i in self.marg.keys():
					text_file.write("P("+i+ ') = ' + str(round(self.marg[i]/float(len(self.Model)), 5)))
					text_file.write('\n')
			text_file.write("\n")			
			text_file.write("Transition probabilities:\n")
			for i in self.statespace:	
				for j in self.statespace:
					text_file.write("P("+j+"|"+i+") = "+str(round((self.trans[i][j]+1)/float((sum(self.trans[i].itervalues())+27)), 5)))
					text_file.write('\n')
			text_file.write('\n')
			text_file.write("Emission probabilities:\n")	
			for i in self.statespace:	
				for j in self.statespace:
					text_file.write("P("+j+"|"+i+") = "+str(round((self.emis[i][j]+1)/float((sum(self.emis[i].itervalues())+27)), 5)))
					text_file.write('\n')	