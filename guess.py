#!/bin/python
import random

#initialize the pseudorandom generator
random.seed()

LOW_END = 0
HIGH_END = 9

random_number = random.randint(LOW_END, HIGH_END)

print("I am thinking of an integer from " + str(LOW_END) + " to " + str(HIGH_END) +".")

#sentinel
still_guessing = True
guessed_number = -1

while still_guessing is True:
    guessed_number_string = input("What number am I thinking of? ")
    try:
        guessed_number = int(guessed_number_string)
    except ValueError:
        print("That's not an integer!")
        continue
    if (guessed_number < LOW_END) or (guessed_number > HIGH_END):
        print("That is not between " + str(LOW_END) +
              " and " + str(HIGH_END) + "!")
    elif guessed_number > random_number:
        print("Sorry, your number is too high. Try again.")
    elif guessed_number < random_number:
        print("Sorry, your number is too low. Try again.")
    elif guessed_number == random_number:
        still_guessing = False

assert guessed_number == random_number
print("You got it! I picked " + str(random_number) + ".")






