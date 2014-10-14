#!/usr/bin/python

def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b

def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b

def multiply(a,b):
	print "MULTIPLY %d * %d" % (a,b)
	return a * b

def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b

print "Let's do some math with the functions we just created"

age = add(25,5)
height = subtract(80,4)
weight = multiply(80, 2)
iq = divide(1500,10)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# Puzzle:

print "So, here is the tricky thing"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print "And that tricky thing now becomes: %d. Could you have done that by hand?" % what

def always_return_what_passed(s):
	return s

value = always_return_what_passed("Awesome!")
print value

raw_value = 24 + 34 / 100 - 1023
new_value_func = subtract(add(divide(34,100), 24), 1023)

if raw_value == new_value_func:
	print "The values are same. Congrats!"
else:
	print "The function response is not right, try again."