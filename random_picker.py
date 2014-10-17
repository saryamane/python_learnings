#!/usr/bin/python

import random
from time import sleep
import sys

decision = raw_input("Use default list? (Y/N)")

if decision == "Y" or decision == "y":
	# Use the default list or ask for a new list.
	print "These are the people participating in the raffle."

	player_name = ['Rajesh', 'Raj', 'Arshad', 'Vamshi', 'Simo', 'Samir','Praveen', 'Ekta',
	'Ishwarya', 'Kishore', 'Raviteja', 'Janardhan', 'Chandra', 'Maya', 'Harish']

	total_players = len(player_name)
	print "I am using these in the raffle. If they are not correct press CTRL-C"
	for i in range(total_players):
		print player_name[i]
elif decision == "N" or decision == "n":
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
else:
	print "You have been only asked to select Y or N."
	sys.exit()

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
sleep(5)
# Give the random generator name picker.
print player_name[modulo_of_list]
sleep(2)

print
print "Congragulations %s!!!" % player_name[modulo_of_list]
sleep(2)

print
print "Everyone, thank you for playing, now get back to work!"
# End of program

