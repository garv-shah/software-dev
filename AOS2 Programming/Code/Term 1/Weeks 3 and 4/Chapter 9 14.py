import random

player_money = 100
choice_list = ['h', 't']
game_over = False

print(f"Welcome to the heads and tails game! You have ${player_money} to play with.")

while game_over is False:
    guess = input('Heads (h) or tails (t)?\n')
    random_choice = random.choice(choice_list)

    if guess == random_choice:
        player_money += 9
        print('You guessed correctly! You win $9.')
        if player_money >= 200:
            print('You have $200! You win the game!')
            game_over = True
            break
    else:
        player_money -= 10
        print('You guessed incorrectly! You lose $10.')
        if player_money <= 0:
            print('You have $0! You lose the game!')
            game_over = True
            break

    print(f'You have ${str(player_money)}.')
