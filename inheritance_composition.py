#!/usr/bin/python

class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

	def override(self):
		print "PARENT override()"

	def __init__(self):
		pass

class Child(Parent):
	
	def implicit(self):
		print "CHILD implicit()"

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

	def override(self):
		print "CHILD override()"

	def __init__(self, stuff):
		self.stuff = stuff
		super(Child, self).__init__()

dad = Parent()
son = Child(Parent)

dad.implicit()
son.implicit()

"""If you put functions in the base class then all the child subclasses 
will inherit it."""

dad.override()
son.override()

dad.altered()
son.altered()

print "Now moving to the composition of the example."

print "\n"

class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class SomeChild(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "SomeChild override()"

	def altered(self):
		print "SomeChild, BEFORE OTHER altered()"
		self.other.altered()
		print "Somechild, AFTER OTHER altered()"

someson = SomeChild()

someson.implicit()
someson.override()
someson.altered()

print """The above example is not is-a inheritance relationship. 
this is a has-a relationship where some child has a other, 
that is used to get the work done."""

print "\n"

print "The other could either be a class or a module named other.py"

print """Inheritance solves this problem by creating a mechanism for you to 
have implied features in base classes. Composition solves this by giving you 
modules and the ability to call functions in other classes."""

print """Use composition to package code into modules that are used in many different 
unrelated places and situations."""

print

print """In inheritance the base class code is assigned to the sub-class at 
compile time, hence you cannot leverage the runtime code association which composition can provide."""
