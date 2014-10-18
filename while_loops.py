#!/usr/bin/python

def main(incremental):
	i = 0
	numbers = []
	stopping_point = 6
	incre_value = incremental

	while i < stopping_point:
		print "At the top i is %d" % i
		numbers.append(i)
		i += incre_value
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers:"

	for num in numbers:
		print num

def using_for_loop():
	i = 0
	numbers = []
	stopping_point = 10
	for i in range(0, stopping_point):
		if (i % 2 == 0):
			numbers.append(i)
	print numbers

if __name__ == "__main__":main(2)

using_for_loop()