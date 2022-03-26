import sys


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'xznlwebgjhqdyvtkfuompciasr'


password = 'password'
guess = input('enter the password:')
if guess == password:
    option = input('Do you want to encode or decode y for encode n for decode: ')
    if option == 'y':
        secret_message = input('Enter your message: ')
        secret_message = secret_message.lower()
        for c in secret_message:
            if c.isalpha():
                print(key[alphabet.index(c)], end='')
            else:
                print(c, end='')
    else:
        hidden_message = input('\nEnter the encrypted message:')
        hidden_message = hidden_message.lower()

        for i in hidden_message:
            if i.isalpha():
                print(alphabet[key.index(i)], end='')
            else:
                print(i, end='')
else:
    print('incorrect password')
    sys.exit()
