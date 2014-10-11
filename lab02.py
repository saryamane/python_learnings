#!/usr/bin/python

class Egg:
	def __init__(self, kind="fried"):
		self.kind = kind

	def whatKind(self):
		return self.kind

def main():
	fried = Egg()
	scrambled = Egg("scrambled")
	print(fried.whatKind())

	num = float(42.0) / 9
	print(type(num), num)

	s=r"This is a \nstring! for number: {}".format(num)
	m = "This is another way to get the number: %f" %(num)
	# Format is the method of the string object.
	# r forces it to make it raw.
	"""
	This is the documentation,
	this goes for line after line
	for writing more text after the other
	 """
	print(s)
	print
	print(m)

	""" New session on the variables of tuple"""
	x = (1,2,3)
	print(type(x),x)
	for i in x:
		print(i)
	"""Now the time for lists"""
	y = [1,2,3]
	y.append(4)
	y.insert(2,7)
	print(type(y), y)
	"""Now for the string"""
	p='string'
	print(type(p),p[2:4])

if __name__ == "__main__":main()