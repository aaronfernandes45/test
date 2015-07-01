max_height = 8
max_breadth = 8


class robot:
	

	def __init__(self):
		print ("test")
		self.grid_height = 4
		self.grid_breadth  = 4

	def printing(self):
		print (max_height)
		print (max_breadth)
		print (self.grid_height)



r = robot()

r.printing()

class user:

	def __init__(self):
		self.inputss = 'w'
		self.user_input()

	def user_input(self):
		while self.inputss != 'q':
			self.inputss  = input ("Enter direction : ")
			print(self.inputss)


u = user()