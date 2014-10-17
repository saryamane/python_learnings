#!/usr/bin/python

import random
from time import sleep
import sys

# Ask user for the number of players.

print "How many people eligible to play in lottery?"

total_players = int(raw_input("> "))

# Create a list of those many numbers.

# Declare an list variable with names of participants.
# Ask users for inputting the name.

player_name = [0] * total_players

for people in range(total_players):
	counter = people + 1
	print "Name of player %d? " % counter
	input_value = raw_input("> ")
	player_name[people] = input_value


# Ask user if they want to give any number as the seed?

user_input = raw_input("""Do you want to provide me with a more random number? (Y/N)
(If not it's still fine, you're results will still be random) > """)

if user_input == "Y" or user_input == "y":
	# Take the seed as input, ask user for seed.
	seed_value = int(raw_input("Please provide me with seed value (only numbers) > "))
elif user_input == "N" or user_input == "n":
	seed_value = 1
else:
	print "Only Y or N values allowed"
	sys.exit()

random.shuffle(player_name)

# Multiply that by the random number generator and then use the modulo operator
random_number = int(random.random() * seed_value * 1000)

modulo_of_list = random_number % total_players

print "Here is one random value I got: %d" % random_number

print "And here is the random from the number of list items I got %d" %modulo_of_list

print "And the winner is .... Drumrolls!!!"
print
print
sleep(10)

# Give the random generator name picker.
print player_name[modulo_of_list]

sleep(2)
print
print "End of program, get back to work!"

# End of program

