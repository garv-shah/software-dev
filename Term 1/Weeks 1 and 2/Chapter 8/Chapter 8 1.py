# Write a program that asks the user to enter some text and then counts how many articles are in the text. Articles
# are the words 'a', 'an', and 'the'.

from collections import Counter

text = Counter(input("Enter some text: ").split(' '))
print(f"There are {text.get('a') + text.get('an') + text.get('the')} articles in the text.")
