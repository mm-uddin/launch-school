import random

VALID_CHOICES = ['r', 'p', 'sc', 'l', 'sp']


def prompt(message):
    print(f"==> {message}")


WINNING_COMBOS = {
    'r':     ['sc', 'l'],
    'p':    ['r',     'sp'],
    'sc': ['p',    'l'],
    'l':   ['p',    'sp'],
    'sp':    ['r',     'sc'],
}

def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

def display_winner(player, computer):
    if player_wins(player, computer):
        return 'You win!'
    elif player == computer:
        return "It's a tie!"
    else:
        return "Computer wins!"



player_wins_num = 0
computer_wins_num = 0

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    prompt(f'''Choose "r" for rock, 
    Choose "p" for paper,
    Choose "sc" for scissors,
    Choose "sp" for spock,
    Choose "l" for lizard''')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}, computer chose {computer_choice}")

    winner = display_winner(choice, computer_choice)
    prompt(winner)
    
    if winner == "You win!":
        player_wins_num += 1
    elif winner == "Computer wins!":
        computer_wins_num += 1
    
    print(f'Player wins for {player_wins_num} times')
    print(f'Computer wins for {computer_wins_num} times')    
    

    if player_wins_num == 3 or computer_wins_num == 3:
        if player_wins_num > computer_wins_num:
            prompt("You are the grand winner")
        elif computer_wins_num > player_wins_num:
            prompt("Computer is the grand winner")

        break