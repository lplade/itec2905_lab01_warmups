#!/bin/python

# Write a program that turns a sentence into camel case. The first word is
# lowercase, the rest of the words have their initial letter capitalized, and
# all of the words are joined together. For example, with the input
# "fOnt proCESSOR and ParsER", your program will output
# "fontProcessorAndParser".
#
# Optional extra question: print a warning message if the input will not
# produce a valid Python variable name. You don't need to be exhaustive in
# checking, but test for a few common issues, such as starting with a number,
# or containing invalid characters such as # or + or ".
#
# Test your program, and comment your code.

print("Enter a sentence and I will camelCase it.")
input_sentence = input("> ")

new_word = False
output_sentence = ""

#loop over that string
for char in input_sentence:
    if char == ' ':
        new_word = True
        # just flip flag, ignore for output purposes
    else:
        if new_word is True:
            output_sentence += char.upper()
        else:
            output_sentence += char.lower()
        new_word = False
    #TODO test for legit characters

print("Here is your string in camelCase:")
print(output_sentence)
