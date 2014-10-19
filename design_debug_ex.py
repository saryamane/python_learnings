#!/usr/bin/python

def main():
	if 3 < 2:
		print "End of the world"
	else:
		pass
	# 	#print "Not coming here."

def f123():
	yield 1
	yield 2
	yield 3


if __name__ == "__main__": main()

a,b,c = f123()
print a, b, c

# Yield will retun an iterable. This is very powerful in python.

def some_function():
	for i in xrange(4):
		yield i

for i in some_function():
	print i

print

print "Moving to exploring as:"

class SomeClass:
	class_dict = {0:9,1:8,2:7,3:6}

newClass = SomeClass()

thedict = newClass.class_dict

for n in thedict:
    # thedict[n] = thedict[n] + 1
    # print(thedict[n])
    print "The key value is %d and its corresponding value is %d" % (n, thedict[n])

print(newClass.class_dict)

print

print "Moving to assert usage in python"

value = int(raw_input("Enter a positive number: "))
assert(value >= 0), 'Only positive numbers are allowed'

""" It tells you to check that the condition is true for sure, used for debugging purposes"""

dictio = [1,2,3,4,5]
print dictio
del dictio[4]
print dictio
print "See I have deleted the 5th element position from the list."

exec('print (5)')
exec 'print "hello"'

global X

X = 15

def only_print():
	print X

only_print()

print

print "Trying out the is keyword in python"

print """'is' tests for identity, not equality. That means Python simply compares the memory address a object resides in."""

x, y = 15, 30
z = y

if y is z:
	print "My memory addresses are the same"
else:
	print "No, I am very different"

val = 1 is 1 # This returns True as they both are identical.
print val

print

print "Let's dig deeper into pythons anonymous functions using lambdas"

s = lambda y: y * y

print s(3)

print """python functions not bound by any name, they are created at runtime. Their construct is called
lambda. This is a very powerful feature and is used typical functional concepts like
filter(), map(), reduce().
"""

def make_incrementor(n): return lambda x: x + n
f = make_incrementor(4)
g = make_incrementor(6)

print f(42), g(50)
print make_incrementor(22)(33)

print "More on lambdas"

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print "The value of foo is", foo
print filter(lambda x: x % 3 == 0, foo)
print map(lambda x: x * 2 + 10, foo)
print reduce(lambda x, y: x + y, foo)

print "Now lets get all prime numbers between 1 to 50 using lambdas"

nums = range(2, 50)
for i in range(2, 8):
	nums = filter(lambda x: x == i or x % i, nums)

print nums

# Write a simple map reduce function in python on a sentence.

sentence = 'It is raining cats and dogs'
words = sentence.split()
print words
lenghts = map(lambda words: len(words), words)
print lenghts

print "This has printed the number of letters that word has printed."

