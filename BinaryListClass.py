import math

class List_Binary(object):
	
	def __init__(self, lis):

		self.lis = lis
		self.lis.sort()
		self.pos = math.floor((len(lis) - 1) / 2)
		self.ans = ""

	def position(self):
		return self.lis[self.pos]

	def move_right(self):
		self.pos += 1

	def move_left(self):
		self.pos -= 1

	def check_pos(self):
		if (self.pos < len(self.lis) - 1) or (self.pos > -1):
			return True
		else:
			False

	def check_val(self, x):
		if self.position < x:
			return 1
		elif self.position > x:
			return 2
		else:
			return 3

def Binary_Search(lis,x):
	stage = List_Binary(lis)
	tmp = 0
	while tmp != 3 or stage.check_pos() != False:
		if stage.check_val(x) == 1:
			stage.move_right()
			tmp = stage.check_val(x)
			print tmp
		elif stage.check_val(x) == 2:
			stage.move_left()
			tmp = stage.check_val(x)
			print tmp
		else:
			tmp = stage.check_val(x)
			print tmp
	if tmp == 3:
		print 'True'
	else:
		print 'False'
l  = [2,34098304,1,5766565,3223,8,453534,19,2003,0,9547959]
Binary_Search(l,2)