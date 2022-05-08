# ################################################################# #
# ## #                                             Unit 3 Software Development
# ## #                                              Programming SAC Module 1
# ## #                                                          Daniel Smith
# ## #
# ## #                                                           16/03/2022
# ## #
# ## #                                                      Required Modules:
# ## #                                                         	⁃	random
# ## #                                                          ⁃	string
# ## #                                                        	⁃	os
# ## #                                                        	⁃	fontstyle
# ## #
# ## #################################################################

try:
    import random, string, os, fontstyle
except ModuleNotFoundError:  # Escapes error and kills program if a required module is not found
    print(fontstyle.apply("Error: Unable to Import Required Modules", "red/bold/underline"))
    exit()
os.system("clear")

randLetter = string.ascii_uppercase[random.randint(0, 25)]  # Establish Random Letter
print("Random letter is {}".format(randLetter))
randPos = random.randint(0, 4)  # Establish Random Position
print("Random position is {}".format(randPos))

try:
    randString = ["_", "_", "_", "_", "_"]
    randString[randPos] = randLetter
    print("{} {} {} {} {}".format(randString[0], randString[1], randString[2], randString[3], randString[4], ))
except IndexError:  # Escapes error and kills program if random string hasn't been properly formed or the print statement can't be executed
    print(fontstyle.apply("Error Creating Random String", "red/bold/underline"))
    exit()

try:
    print("\nMatching Words:")
    with open("task1words.txt", "r") as textFile:
        words = 0  # Establish a basic counter for matching words
        lines = textFile.readlines()
        for word in lines:
            if word[randPos] == randLetter.lower():
                print(word, end="")
                words += 1  # Adds 1 to matching word counter
        if words == 0:
            print(fontstyle.apply("No Matches", "blue/bold"))
        else:  # If all lines have been read and <= 1 word matches
            print(fontstyle.apply(
                "\nThere are {} word(s) that match {} in position {}".format(words, randLetter, randPos), "green/bold"))
except FileNotFoundError:  # Escapes error and kills program if no file matching 'task1words.txt' is found
    print(fontstyle.apply("Error: No File Found", "red/bold/underline"))
    exit()
