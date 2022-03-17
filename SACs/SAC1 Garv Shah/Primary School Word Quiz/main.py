import csv
import random
import string
import os


correct_answers = 0
question_list = []
for file in os.listdir("./"):
    if file.endswith(".csv"):
        # Loads the data from a csv file if it exists
        try:
            with open(file, "r") as csv_file:
                # Creates a dictionary from the csv file
                reader = csv.DictReader(csv_file)
                question_list = list(reader)
                csv_file.close()

                for question in question_list:
                    print(question)
                    if not all(value is not None for value in question.values()):
                        print("woah woah woah woah")

                if reader.fieldnames != ['topic', 'question', 'optionA', 'optionB', 'optionC', 'optionD', 'answer']:
                    print(f"The provided file {file} is not in the correct format to be used with this program. "
                          f"Please input a csv file with the correct question format, including the headers 'topic', "
                          f"'question', 'optionA', 'optionB', 'optionC', 'optionD' and 'answer'")
                    exit()
        except FileNotFoundError:
            print("Sorry! There was no csv file found in the local directory, please add questions to continue.")
            exit()

if input("Would you like to filter by topic? (y/n) ").lower() == "y":
    available_topics = set([question['topic'].lower() for question in question_list])
    print(f"Available topics: {', '.join(available_topics)}")

    while True:
        topic = input("Please enter the topic you would like to filter by: ")
        if topic.lower() in available_topics:
            question_list = [question for question in question_list if question["topic"].lower() == topic]
            break
        else:
            print("Sorry! That topic is not available, please try again.")
            continue

for x in range(len(question_list)):
    question = question_list[x]
    print(f"Topic: {question['topic']}")
    print(f"Question: {x + 1}")
    print(question['question'])
    print(f"A - {question['optionA']}")
    print(f"B - {question['optionB']}")
    print(f"C - {question['optionC']}")
    print(f"D - {question['optionD']}")
    if input("Enter the letter of the correct answer: ").lower() == question['answer'].lower():
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect!")
        print(f"The correct answer was {question['answer']}")

    print()

print(f"You got {correct_answers} out of {len(question_list)} correct!")
