#!/usr/bin/python

print "I will now count my chickens:"
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "Is it true that 3 + 2 < 5 -7? "

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it is false."

print "How about some more"

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "Moving to the new exercise of variables with maths"

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have about", passengers, "passengers to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"

print

print "Moving now to using variables within the print statements."

name = "Samir C Aryamane"
age = 30 # not a lie
height = (5 * 12) + 6 # converting it into inches.
height_in_cms = float(height) * 2.54
weight = 185 # lbs
weight_in_kg = round(float(weight) * 0.45,2)
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s" % name
print "He's %d inches tall" % height
print "He's %d pounds heavy" % weight
print "Actually that is not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s, but that depends on what coffee he had that day" % (teeth)

# This line is the one that does the math.
print "If I add %d, %d and %d I would get %d." % (age, height, weight, age + height + weight)

# This is the line that prints my measurements in UK metric system.
print "According to Indian metric system my weight is %.2f kgs and my height is %.2f centimeters" %(weight_in_kg, height_in_cms)

my_raw_string = 'this is \ absured and it prints anything # \$, \n is also fine and printed ok. This will even print the single quotes here.'

print "Lets print this raw string whatever it is: %r" %(my_raw_string)

print

print "Moving to exercise 6 for strings and using variables formatting"

print

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = " a string with a right side."

print w + e

print

print "More priniting with exercise 8, doing this while watching NFL. Go packers!"

print "Marry had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # This prints dots for 10 times.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11= "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# Can also so something like this.

print end1 + end2 + end3 + end4 + end5 + end6, end7 + end8 + end9 + end10 + end11 + end12

print 
print "More printing printing and more printing, but complex this time"

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True, False, False, True)
print formatter %(formatter, formatter, formatter, formatter)
print formatter % (
		"I had this thing",
		"That you could type up right",
		"But it didn't sing",
		"So I said goodnight."
	)


print

print "Ex9: More weird printing ahead"

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print "Here are the days: ", days
print "And here are the months: ", months

print """There is something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines, or maybe even better 5, 6 or 7
but we will end here """

print

print "Final ex10 about printing with escape sequences"

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat


# fun code to try out
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
