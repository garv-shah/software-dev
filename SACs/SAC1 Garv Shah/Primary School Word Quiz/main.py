import csv
import os
import sys

# declaration of global variables
correct_answers = 0
question_list = []


def read_and_validate_csv():
    """
    Goes through all the files in the local directory and if the file ends with .csv, it opens it
    """

    global question_list

    for file in os.listdir("./"):
        if file.endswith(".csv"):
            with open(file, "r") as csv_file:
                # Once the file is opened, it creates a list with nested dicts with the form [{}, {}, {}]
                # This is saved to the question_list variable
                reader = csv.DictReader(csv_file)
                question_list = list(reader)
                csv_file.close()

                # The following all handle errors

                # This makes sure the headers are valid, making sure the correct headers are present
                if reader.fieldnames != ['topic', 'question', 'optionA', 'optionB', 'optionC', 'optionD', 'answer']:
                    print(f"The provided file {file} is not in the correct format to be used with this program. "
                          f"Please input a csv file with the correct question format, including the headers 'topic', "
                          f"'question', 'optionA', 'optionB', 'optionC', 'optionD' and 'answer'")
                    sys.exit()

                # This loop goes through the question list to make sure they are all valid
                for x in range(len(question_list)):
                    # Checks if any of the entries are of type None.
                    # This would mean that the question/row is missing a value for a header, meaning it's not filled out
                    # This is not ideal for our use case, as all rows must have data for all headers
                    if any(value is None for value in question_list[x].values()):
                        key_list = list(question_list[x].keys())
                        value_list = list(question_list[x].values())
                        # The field missing is calculated by finding the index of the first None in a list of values for
                        # the question. This index is then put into the keys (they have a one to one mapping),
                        # which allows us to find the key with the None value
                        print(f"Sorry, there's an error with your csv file! Namely, row {x + 1} is missing a value "
                              f"for the field {key_list[value_list.index(None)]}. Please fix this and try again.")
                        sys.exit()
                    # This statement makes sure that the answer field is valid. The answer shouldn't be the full text
                    # answer, such as "5 sides", but should rather be the associated letter for the question
                    elif question_list[x]["answer"].lower() not in ['a', 'b', 'c', 'd']:
                        print(f"Sorry, there's an error with your csv file! Namely, row {x + 1}'s answer is entered as "
                              f"{question_list[x]['answer']} when the answer field must be a, b, c, or d.")
                        sys.exit()

                # Finally, this makes sure that question_list does not equal []. This would mean that the file has the
                # correct headers, but no questions in it, so the user is prompted to add them
                if not question_list:
                    print(f"The provided file {file} doesn't have any questions in it. Please add some to continue.")
                    sys.exit()

    # This is the same statement as the one above, but if question_list = [] *and* the above didn't run,
    # it means that no csv file was found. This is because the original question_list would be unmodified,
    # so it is in its initial state.
    if not question_list:
        print("No csv file was found in the local directory. Please create a csv file with questions to continue.")
        print("The headers of the csv file should be as follows:")
        print("topic, question, optionA, optionB, optionC, optionD, answer")
        sys.exit()


def filter_by_topic():
    global question_list

    user_filter = input("Would you like to filter by topic? (y/n) ").lower()
    if user_filter in ("y", "yes"):
        # Gets available topics by getting the topics key/value from each dict (converted to a set to avoid repeats)
        available_topics = set([question['topic'].lower() for question in question_list])
        print(f"Available topics: {', '.join(available_topics)}")

        # This while loop will keep prompting the user until they enter a valid topic
        # If a valid topic is given, the loop is broken. If not, the loop starts again, and they are prompted again
        while True:
            topic = input("Please enter the topic you would like to filter by: ")
            if topic.lower() in available_topics:
                # creates a new list of questions, only if the topic key/value is the one selected by the user
                question_list = [question for question in question_list if question["topic"].lower() == topic]
                break
            print("Sorry! That topic is not available, please try again.")
            continue


def question_loop():
    global correct_answers

    # Main loop of questions
    for x in range(len(question_list)):
        question = question_list[x]
        print(f"Topic: {question['topic']}")
        print(f"Question: {x + 1}")
        print(question['question'])
        print(f"A - {question['optionA']}")
        print(f"B - {question['optionB']}")
        print(f"C - {question['optionC']}")
        print(f"D - {question['optionD']}")

        # Similar to above, prompts user indefinitely until they enter a valid answer: a, b, c, or d
        # .lower is used throughout the file to make sure that the user's input is not case-sensitive
        while True:
            user_answer = input("Enter the letter of the correct answer: ").lower()
            if user_answer in ['a', 'b', 'c', 'd']:
                if user_answer == question['answer'].lower():
                    print("Correct!")
                    correct_answers += 1
                else:
                    print("Incorrect!")
                    print(f"The correct answer was {question['answer']}")
                break
            print("Sorry! Your input was not a valid answer. Please choose from a - d.")
            continue

        print()

    print(f"You got {correct_answers} out of {len(question_list)} correct!")


if __name__ == "__main__":
    read_and_validate_csv()
    filter_by_topic()
    question_loop()
