#!/usr/bin/python

# Transfer the ordinal number to cardinal number by subtracting one from it.
# ordinal == ordered, 1st.
# cardinal == cards at random, 0.

def main():
	animals = ['bear','python','peacock','kangaroo','whale','platypus']
	print "The animal at 1 is %s" % animals[1]
	print "The thrid animal is %s" % animals[2]
	print "The first animal is %s" % animals[0]
	print "The animal at 3 is %s" % animals[3]
	print "The fifth animal is %s" % animals[4]
	print "The animal at 2 is %s" % animals[2]
	print "The sixth animal is %s" % animals[5]
	print "The animal at 4 is %s" % animals[4]


if __name__ == "__main__": main()