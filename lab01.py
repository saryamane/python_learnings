#!/usr/bin/python3

def main():
	print("This is the main function")
	func()
	func(8)
	func(5)

def func(a=1):
	for i in range(a,10):
		print (i)
	print("Comming out of the range function")

if __name__ == "__main__": main()