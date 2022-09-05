import random
from time import sleep

choices = ['rock', 'paper', 'scissors']

rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_wins = 0
computer_wins = 0


def print_standings():
    global player_wins
    global computer_wins
    print(f'''
    The current standings are:
    Player wins:{player_wins}
    Computer wins:{computer_wins}
    ''')

print("\nLet's play Rock, Paper, Scissors!\n")

while True:

    player_choice = input('''
    
    Choose a weapon! Rock, Paper, or Scissors  
            
    Make your selection: ''')
    player_choice = player_choice.lower()
    while player_choice not in choices:
        player_choice = input('    The choices are rock, paper, or scissors...: ')
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        print(f'\n    You both chose {player_choice}. Game is a draw.\n')
        print_standings()
        keep_going = input('    Do you want to keep playing? Type quit to exit or press [Enter] to continue. ')
        if keep_going.lower() == 'quit':
            break
        else:
            continue
    elif player_choice == 'rock' and computer_choice == 'paper':
        print(rock_art)
        print("\n    It's rock versus...\n")
        sleep(2)
        print(paper_art)
        print(f'\n    Computer chose {computer_choice}! You lose!\n')
        computer_wins += 1
        print_standings()
        keep_going = input('    Do you want to keep playing? Type quit to exit or press [Enter] to continue. ')
        if keep_going.lower() == 'quit':
            break
        else:
            continue
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print(rock_art)
        print("\n    It's rock versus...\n")
        sleep(2)
        print(scissors_art)
        print(f'\n    Computer chose {computer_choice}! You win!\n')
        player_wins += 1
        print_standings()
        keep_going = input('    Do you want to keep playing? Type quit to exit or press [Enter] to continue. ')
        if keep_going.lower() == 'quit':
            break
        else:
            continue
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print(scissors_art)
        print("\n    It's scissors versus...\n")
        sleep(2)
        print(rock_art)
        print(f'\n    Computer chose {computer_choice}! You lose!\n')
        computer_wins += 1
        print_standings()
        keep_going = input('    Do you want to keep playing? Type quit to exit or press [Enter] to continue. ')
        if keep_going.lower() == 'quit':
            break
        else:
            continue
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print(scissors_art)
        print("\n    It's scissors versus...\n")
        sleep(2)
        print(paper_art)
        print(f'\n    Computer chose {computer_choice}! You win!\n')
        player_wins += 1
        print_standings()
        keep_going = input('    Do you want to keep playing? Type quit to exit or press [Enter] to continue. ')
        if keep_going.lower() == 'quit':
            break
        else:
            continue
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print(paper_art)
        print("\n    It's paper versus...\n")
        sleep(2)
        print(scissors_art)
        print(f'\n    Computer chose {computer_choice}! You lose!\n')
        computer_wins += 1
        print_standings()
        keep_going = input('    Do you want to keep playing? Type quit to exit or press [Enter] to continue. ')
        if keep_going.lower() == 'quit':
            break
        else:
            continue
    elif player_choice == 'paper' and computer_choice == 'rock':
        print(paper_art)
        print("\n    It's paper versus...\n")
        sleep(2)
        print(rock_art)
        print(f'\n    Computer chose {computer_choice}! You win!\n')
        player_wins += 1
        print_standings()
        keep_going = input('    Do you want to keep playing? Type quit to exit or press [Enter] to continue. ')
        if keep_going.lower() == 'quit':
            break
        else:
            continue
