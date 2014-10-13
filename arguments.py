#!/usr/bin/python

from sys import argv
import sys

try:
	script, first, second, third = argv
except ValueError as v:
	print "I am expecting 3 input params, but looks like this is not the case!", v
	sys.exit() # This is how you exit out of the python program.

print "The script is called: ", script
print "You're first variable is: ", first
print "You're second variable is: ", second
print "You're third variable is: ", third

print "Now give me your Age, please? ",
age = raw_input()

print "Oh my! You are so old, you are %s years old" % (age)

height = raw_input("And your height is? ")
print "You are not so tall with that %s height" % (height)