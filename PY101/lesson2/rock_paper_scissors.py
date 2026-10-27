'''
Rules:
If player a chooses rock and player b chooses scissors, player a wins.
If player a chooses paper and player b chooses rock, player a wins.
If player a chooses scissors and player b chooses paper, player a wins.
If both players choose the same item, neither player wins. It's a tie.

'''
import random


print("RCOCK-----PAPER-----SCISSORS")
print("-----------------------------------------")
print("Welcome to the Game!")
print("When asked to select, use : r for Rock, p for Paper and s for Scissors")

while True:
    print('Select your option: ')
    user_choice = input()

    computer_choice = random.choice(["r", "p", "s"])

    print(user_choice)
    print(computer_choice)
    winner = ''
    
    if (user_choice == 'r' and computer_choice == "s"):
        winner = "user"
    elif (user_choice == 'p' and computer_choice == 'r'):
        winner = 'user'
    elif (user_choice == 's' and computer_choice == 'p'):
        winner = 'user'
    elif (user_choice == computer_choice):
        winner = None
    else:
        winner = "Computer"

    print(f'This round of game was won by {winner}!')

    print('Do you want to play another round? y/n')
    game_continue = input()
    while True:
        if game_continue == 'y' or game_continue == 'n':
            break
        print('Please select "y" or "n"')
        game_continue = input()
    if game_continue[0] == 'n':
        break
print('Game ends!!!!')