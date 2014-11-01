#!/usr/bin/python

## Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
	pass

##?? Dog is-a Animal

class Dog(Animal):

	def __init__(self, name):
		#?? Dog has-a name attribute
		self.name = name

##?? Cat is-a Animal

class Cat(Animal):

	def __init__(self, name):
		##?? Cat has-a name attribute
		self.name = name

##?? Person is-a object

class Person(object):

	def __init__(self, name):
		##?? Person has-a name attribute
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

##?? Employee is-a Person

class Employee(Person):

	def __init__(self, name, salary):
		##??  hmm, what is this strnage magic?
		## It is referencing the super class attribute of Person.
		super(Employee, self).__init__(name)
		##?? Employee has-a salary attribute
		self.salary = salary

## ?? Fish is-a object

class Fish(object):
	pass

##?? Salamon is-a Fish

class Salmon(Fish):
	pass

##?? Halibut is a Fish
class Halibut(Fish):
	pass

## rover is-a Dog

rover = Dog("Rover")

##?? satan is a Cat

satan = Cat("Satan")

##?? Mary is-a Person

mary = Person("Mary")

##?? Mary has-a pet which is-a Cat

mary.pet = satan

## ?? frank is-a Employee has-a name Frank and has a salary of 120000

frank = Employee("Frank",120000)

#?? Frank which is-a person also has-a pet which is-a Dog

frank.pet = rover

## ?? flipper is-a Fish

flipper = Fish()

##?? crouse is-a Salmon

crouse = Salmon()

##?? harry is-a Halibut

harry = Halibut()