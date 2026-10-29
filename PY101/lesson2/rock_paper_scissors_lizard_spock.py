import random

VALID_CHOICES = ['r', 'p', 'sc', 'l', 'sp']


def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    
    if ((player == "r" and computer == "sc") or
        (player == "r" and computer == "l") or
        (player == "p" and computer == "r") or
        (player == "p" and computer == "sp") or
        (player == "sc" and computer == "p") or
        (player == "sc" and computer == "l") or
        (player == "l" and computer == "p") or
        (player == "l" and computer == "sp") or
        (player == "sp" and computer == "r") or
        (player == "sp" and computer == "sc")):
        return ("You win!")
    elif ((player == "sc" and computer == "r") or
          (player == "l" and computer == "r") or
          (player == "r" and computer == "p") or
          (player == "sp" and computer == "p") or
          (player == "p" and computer == "sc") or
          (player == "l" and computer == "sc") or
          (player == "p" and computer == "l") or
          (player == "sp" and computer == "l") or
          (player == "r" and computer == "sp") or
          (player == "sc" and computer == "sp")):
        return ("Computer wins!")
    else:
        return ("It's a tie!")


player_wins = 0
computer_wins = 0

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
        player_wins += 1
    elif winner == "Computer wins!":
        computer_wins += 1
    
    print(f'Player wins for {player_wins} times')
    print(f'Computer wins for {computer_wins} times')    
    

    if player_wins == 3 or computer_wins == 3:
        if player_wins > computer_wins:
            prompt("You are the grand winner")
        elif computer_wins > player_wins:
            prompt("Computer is the grand winner")

        break