#!/usr/bin/python

val = None
print val

if val is None:
	print "This is true"
else:
	pass

print "Let's dig further into the escape sequences"

val = 45
neg_num = -100
large_num = 10000000

print "The octal value of 45 is %o" % val
print "The unsigned value is represented as %u" % neg_num
print "the hexa number for 45 is represented as %x" % val
print "The exponential notation is %e or we can also use %E" % (large_num, large_num)
print "Double percent sign is used for showing percentages: %d%%" % val

print

print "Now moving to math operators which we haven't seen so far."

x = 5
x **= 2
print x
# ** means the exponent value.
# // means the floor division.

val = 2 // 4
print val

print "hi"; print "there"

rem = 75
rem %= 4

print rem

num = 45 

print "Printing with d the number is: %d" % num
print "Printing with i which is supposed to be the same: %i" % num
