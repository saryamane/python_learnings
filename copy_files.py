#!/usr/bin/python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

# Can we do the below from two lines into one line? think?

# in_file = open(from_file)
# indata = in_file.read()

# My try is something like this.

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)

print "Ready? hit the RETURN to continue, CTRL-C to abort."

raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
#in_file.close()