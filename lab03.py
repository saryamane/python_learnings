#!/usr/bin/python

def main():
	#print("This is the main function")
	'''This is the dictionary object'''
	d = {'one':1, 'two':2, 'three':3}
	for k in sorted(d.keys()):
		print(k,d[k])

	print("Moving to other way of defining the dictionary")

	x = dict(
		one=1,
		two=2,
		three=3,
		four='four'
		)
	x['five']=5

	for i in sorted(x.keys()):
		print(i, x[i])

	v = 'seven'
	if v == 'one':
		print ('v is one')
	elif v == 'two':
		print ('v is two')
	elif v == 'three':
		print('v is three')
	else:
		print('v is something else')

	"""Moving to multiple choices like switch or case"""

	choices = dict(
		one = 'first',
		two = 'two',
		three = 'three',
		four = 'four'
	)
	v = 'seven'
	print('v is '+choices.get(v,'something else'))
	a,b = 0,1
	v = 'this is true' if a < b else 'this is not true'
	print v

	while b < 100:
		print(b)
		a,b = b, a+b

	fh = open('lines.txt')
	for index, i in enumerate(fh.readlines()):
		print(index, i)


	c = 'This is a string'
	for i in c:
		if i == 's': continue
		else: print i
	else:
		print 'More string'


if __name__ == "__main__":main()