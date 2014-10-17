#!/usr/bin/python

people = 20
cats = 30
dogs = 15

if people < cats:
	print "To many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less tha or equal to dogs."

if people == dogs:
	print "People are dogs."


print

print "Now moving on some car if-else loops"

people = 3
cars = 40
trucks = 15

# If multiple elif blocks are true, then it will run only the first one.

if cars > people:
	print "We should take cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."

if people > trucks and cars > trucks:
	print "We are really brave to try this."
else:
	print "We are doomed."

