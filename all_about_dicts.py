#!/usr/bin/python

# create a mapping of state to abbreviation

states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities

print '-' * 10
print "NY state has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict.

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated as %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s state has the %s as the city" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbrevated as %s and has %s as the city" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there

state = states.get('Texas') # Lookups based on the key within the dict

if not state:
	print "Sorry, no Texas!"

# get a city with a default value
city = cities.get('TX', 'Does not exists') # Usage of the defualt value if the key is not found in the dict
print "The city for the state 'TX' is: %s" % city


