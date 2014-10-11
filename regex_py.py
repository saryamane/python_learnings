#!/usr/bin/python

import re

def main():
	print ("This is the main function body")
	try:
		fh = open('xlines.txt')
		pattern = re.compile('this',re.IGNORECASE)
		'''This compiles the regex only once before the loop starts'''
		for i in fh:
			match = re.search(pattern,i)
			if match:
				print(match.group())
	except IOError as e:
		print ('The file is not present, here is the error ',e)


if __name__ == "__main__":main()


