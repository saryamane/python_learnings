#!/usr/bin/python

print """Think of a classes as a way of grouping functions and data and place
them inside a container so that you can access them with a dot operator.

Classes can be thought of ways of being a specialized dictionary that can store 
a python code for you.
"""

class myStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"
		self.jumbo = "I am watching 'Everybody loves RAYMOND'"

	def apple(self):
		print "I AM CLASSY APPLES!"

print """When you instantiate a class you get a object
You instantiate a class by calling the class like it's a function
"""

thing = myStuff()
thing.apple()
print thing.tangerine
print thing.jumbo

print """When you instantiate a class, you get the blueprint of that class within the newly created object"""

myDict = {
	'apples': 'This is big apples',
	'oranges': 'These are tangerine oranges'
}

print myDict['apples']
thing.apple()

print

print "Moving to the song classses"

print '-' * 10

print 

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		self.song = lyrics

	def sing_me_a_song(self):
		for line in self.song:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get seud",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])

hawa_hawaii = Song(["Hawa Hawaii",
					"Hawa Hawaii, this is gonna be awesome",
					"Honolulu is the place to be",
					"Beautiful oceans and sandy beaches"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
hawa_hawaii.sing_me_a_song()

print 

print '-' * 10

print

print """Why do I need self when I make __init__ or other functions for classes?
If you don't have self, then code like cheese = 'Frank' is ambiguous. 
That code isn't clear about whether you mean the instance's cheese attribute,
or a local variable named cheese. With self.cheese = 'Frank' it's very clear
you mean the instance attribute self.cheese."""
