# Ask the user to enter a sentence and print out the third word of the sentence.
# Ask the user to enter a sentence and print out every third word of the sentence.

user_input = input("Enter a sentence: ").split(' ')
print(f"The third word of the sentence is: {user_input[2]}")
print(f"Every third word of the sentence is: {user_input[2::3]}")
