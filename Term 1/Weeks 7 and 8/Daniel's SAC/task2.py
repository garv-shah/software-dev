try:
    import csv,fontstyle,os
except ModuleNotFoundError:
    print(fontstyle.apply("Error: Unable to Load Modules","red/bold"))
    exit()

questionsIndex,correctAnswers = 0,0
choice = ""
topics,questions = [],[]
chosenTopic = ""

def chooseTopic(): # Allows user to choose a specific topic or choose All
    global chosenTopic
    os.system("clear")
    print(fontstyle.apply("What topic would you like to practice: ","bold"))
    print()
    for topic in topics:
        print(" - " + topic)
    print(" - All")
    chosenTopic = input("\nWhat topic would you like to do: ").capitalize()

    if chosenTopic not in topics: # If the User has entered an invalid topic make them try again
        if chosenTopic == "All":
            os.system("clear")
            quiz(chosenTopic) # Start quiz with Chosen Topic
        else:
            chooseTopic()
    else:
        os.system("clear")
        quiz(chosenTopic) # Start quiz with Chosen Topic

def quiz(topic):
    for question in questions:
        if topic != "All":
            if question["topic"] == topic:
                questionFunc(question) # Execute question
            else:
                pass
        else:
            questionFunc(question) # Execute question
    quizEnd() # After all questions, execute the end quiz function

def questionFunc(questionData): # Displays the question to the user and allows answer
    global questionsIndex,correctAnswers
    questionsIndex += 1
    while True:

        print("Question {}".format(questionsIndex))
        print("Topic: {}".format(questionData["topic"]))
        print(questionData["question"])
        print("A - {}".format(questionData["optionA"]))
        print("B - {}".format(questionData["optionB"]))
        print("C - {}".format(questionData["optionC"]))
        print("D - {}".format(questionData["optionD"]))
        answerGiven = input("Enter the letter of the correct answer: ").upper()

        if answerGiven not in ["A","B","C","D"]: # If answer given is not a possible answer
            print(fontstyle.apply("Sorry that wasn't one of the options","blue/bold"))

        elif answerGiven == questionData["answer"]: # Correct
            print(fontstyle.apply("Correct\n","green/bold"))
            correctAnswers += 1
            break

        else: # Incorrect
            print(fontstyle.apply("Incorrect\n","red/bold"))
            break

try:
    with open("task2Data.csv", "r") as textFile:
        data = csv.DictReader(textFile, delimiter=",")
        for row in data:
            if row["topic"] not in topics:
                topics.append(row["topic"])
            questions.append({"topic":row["topic"],"question":row["question"],"optionA":row["optionA"],"optionB":row["optionB"],"optionC":row["optionC"],"optionD":row["optionD"],"answer":row["answer"]})
except FileNotFoundError or IndexError:
    print(fontstyle.apply("Error: Unable to load questions file","red.bold"))
    exit()

def quizEnd(): # Facilitates the end of the program and asks user is they want to play again, otherwise quit
    global correctAnswers,questionsIndex,choice, chosenTopic
    print(fontstyle.apply("You answered {} out of {} questions correctly.","purple/bold").format(correctAnswers,questionsIndex))
    print(fontstyle.apply("Well Done!","purple/bold"))

    while choice != "Y" or choice != "N":
        choice = input(fontstyle.apply("\n\nWould you like to play again? (Y/N)","yellow/bold")).upper()
        if choice == "Y":
            questionsIndex,correctAnswers = 0,0
            choice = ""
            chosenTopic = ""
            chooseTopic() # Go Back to Start
        if choice == "N":
            exit()
        else:
            print(fontstyle.apply("Sorry that wasn't one of the options","blue/bold"))
            quizEnd()

chooseTopic() # Starts program with topic choice screen