max_height = 8
max_breadth = 8


class robot:
	

	def __init__(self):
		print ("test")
		self.grid_height = 4
		self.grid_breadth  = 4

	def modify(self, val):
		if val == 'w':
			if self.grid_height < max_height:
				self.grid_height += 1
		if val == 's':
			if self.grid_height > 0:
				self.grid_height -= 1
		if val == 'd':
			if self.grid_breadth < max_breadth:
				self.grid_breadth += 1
		if val == 'a':
			if self.grid_breadth > 0:
				self.grid_breadth -= 1
		self.printing()


	def printing(self):
		print (self.grid_height)
		print (self.grid_breadth)
		print (" ")



r = robot()
r.printing()


class user:

	def __init__(self):
		self.inputss = 'w'
		self.user_input()

	def user_input(self):
		while self.inputss != 'q':
			self.inputss  = input ("Enter direction : ")
			#print(self.inputss)
			r.modify(self.inputss)





u = user()


