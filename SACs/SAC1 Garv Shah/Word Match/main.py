import random
import string
import os
import sys

# opens word list and saves it to an array
# this was changed from just opening the 'words.txt' file, as if the file has a different name, it doesn't work
# rather, this method searches the local directory for any text file, and opens the first one it finds
words = []
for file in os.listdir("./"):
    if file.endswith(".txt"):
        with open(file, "r") as f:
            words = f.readlines()
            if not all(len(word) == 6 for word in words):
                print("WARNING: invalid text file format. All words must be 5 letters long, followed by a newline.")
                print("If you choose to continue, the program may not work as expected.")
                print("Do you wish to continue? (y/n)")
                if input().lower() == "y":
                    print()
                    continue
                else:
                    sys.exit()
                # the above lines of code check if the input file is valid, and warns the user if it isn't
            break

# gets a random alphabet and gets a random number
alphabet = random.choice(string.ascii_lowercase)
# the string.ascii_lowercase is just a string equal to 'abcdefghijklmnopqrstuvwxyz'
# and the function above chooses a random char
random_number = random.randint(0, 4)

print(f"Random letter is {alphabet}")
print(f"Random position is {random_number}")

blank_array = ['_' for i in range(5)]
# creates an array of 5 underscores: ['_', '_', '_', '_', '_']
blank_array[random_number] = alphabet
print(''.join(blank_array))
# concatenates the array into a string to print

matching_words = []
for word in words:
    try:
        if word[random_number] == alphabet:
            matching_words.append(word)
    except IndexError:
        print("ERROR: The word chosen has less than 5 letters!")
        # Checks if the word has 5 or more letters, and if it doesn't, it prints an error message,
        # but tries to continue as the user already asked it to

# adds all words that match the random letter at the chosen index to an array, which is then looped through and printed

print()
print(f"{len(matching_words)} matching words found!")
print("Matching words:")

for word in matching_words:
    print(word, end="")
    # end="" is needed as the text file already has new lines that have been read,
    # so with the extra newline of print, it would print \n\n and not just \n
