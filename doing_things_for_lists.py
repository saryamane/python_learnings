#!/usr/bin/python

def main():

	ten_things = "Apples Oranges Crows Telephone Light Sugar"

	print "Wait there are not 10 things in that list. Let's fix that."

	stuff = ten_things.split(' ')

	more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

	while len(stuff) != 10:
		next_one = more_stuff.pop()
		print "Adding: ", next_one
		stuff.append(next_one)
		print "There are %d items now." % len(stuff)

	print "There we go: ", stuff

	print "Let's do some things with stuff."

	print stuff[1]
	print stuff[-1] # whoa! fancy
	print stuff.pop()
	print ','.join(stuff) # what? cool!
	print '#'.join(stuff[3:5]) # super stellar!
	stuff.sort()
	print stuff

	print "Use this website to learn about all there is to for Python Lists"
	print "http://www.tutorialspoint.com/python/python_lists.htm"


if __name__ == "__main__": main()