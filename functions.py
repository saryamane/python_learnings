#!/usr/bin/python

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothing!"

"""The variables in your function are not connected
to the variables in your script.
"""

print_two("Samir","Aryamane")
print_two_again("Awesome", "Wave")
print_one("VizCloud")
print_none()

print

print "Moving to the exercise where we are looking at functions and variables together"

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use the variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside it too"

cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math together:"
cheese_and_crackers(amount_of_cheese + 50, amount_of_crackers + 1000)

no_of_cheese_boxes=int(raw_input("Now give me the number of cheese boxes, will you? > "))
no_of_cracker_boxes=int(raw_input("Now give me the number of cracker boxes, will you? > "))

cheese_and_crackers(no_of_cheese_boxes,no_of_cracker_boxes)

def print_names(*args):
	arg1 = args
	print "And I see that you're name is: %r" % arg1
	return arg1


abc = "Dhanu"

print_names("Samir")
print_names(abc)
print_names("Samir"+abc)
print_names("Samir"+"\n"+abc)

""" You can also call the function within a function.
"""

print "Your name is so awesome: %r" %print_names("Samir")