#!/usr/bin/python

from sys import argv
import sys

try:
	script, filename = argv
except:
	print "Not enought parameters passed. Exiting the code..."
	sys.exit()

print "We are going to erase the file: %r" % filename
print "If you don't want that, hit CTRL-C (^C) now"
print "If you do want that, hit RETURN key now"

raw_input("?")

print "Opening the file"
try:
	target = open(filename,'w+') 
	"""We do not need the try and except, 
	as if the file is not present, it will 
	create a new one."""
except:
	print "Filename passed as parameter is not found...exiting."
	sys.exit()

print "Truncating the file. Goodbye!"
target.truncate()
"""Truncate is not needed here as the w option while
opening the file makes the file to be overwritten.
Use the a or a+ option to append to the existing file
if it exists, if it does not, then create a new file
for writing.
"""

print "Now I am going to ask you for 3 lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print ("Now I am going to write these to the file name you provided me earlier.")

""" 6 steps to write to the file is bad practise, instead using 
a single write to the file. Here is my attempt after commenting the
previous code.
"""

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

write_value = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(write_value)

"""What took me a lot of time to grapple with is
that the file was not getting saved to disk
until I close the handler and then re-open the file
for reading purposes. This is very important feature
to note, how the program works."""

print "And finally, we will now close it."
target.close()

print

print "Now is the time to show the world, what inputs you gave me :)"

read_file = open(filename,'r')

""" It is important to note here that just doing
open(filename) will open the file in the default 
read mode which is the same as the above code
command.
"""

# for i in read_file.readlines():
# 	print i

print read_file.read(),

print "Awesome! Now good bye!"


