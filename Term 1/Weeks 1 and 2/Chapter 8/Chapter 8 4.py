# Write a program that asks the user to enter a sentence and then randomly rearranges the words of the sentence.
# Don’t worry about getting punctuation or capitalization correct.

# Do the above problem, but now make sure that the sentence starts with a capital, that the original first word is
# not capitalized if it comes in the middle of the sentence, and that the period is in the right place.

import random

user_input = input("Enter a sentence: ").split(' ')
random.shuffle(user_input)
print(f"Shuffled sentence is: {' '.join(user_input)}.")
