import random
from time import sleep

choices = ["rock", "paper", "scissors"]

rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player_wins = 0
computer_wins = 0


def print_standings():
    global player_wins
    global computer_wins
    print(f"""
    The current standings are:
    Player wins:{player_wins}
    Computer wins:{computer_wins}
    """)


print("\nLet's play Rock, Paper, Scissors!\n")

while True:

    player_choice = input("Choose your weapon: ")
    while player_choice not in choices:
        player_choice = input("The choices are rock, paper, or scissors...: ")
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        print(f"\nYou both chose {player_choice}. Game is a draw.\n")
        print_standings()
        keep_going = input("Do you want to keep playing? Enter y to play again. ")
        if keep_going.lower() == "y":
            continue
        else:
            break
    elif player_choice == "rock" and computer_choice == "paper":
        print(rock_art)
        print("\nIt's rock versus...\n")
        sleep(2)
        print(paper_art)
        print(f"\nComputer chose {computer_choice}! You lose!\n")
        computer_wins += 1
        print_standings()
        keep_going = input("Do you want to keep playing? Enter y to play again. ")
        if keep_going.lower() == "y":
            continue
        else:
            break
    elif player_choice == "rock" and computer_choice == "scissors":
        print(rock_art)
        print("\nIt's rock versus...\n")
        sleep(2)
        print(scissors_art)
        print(f"\nComputer chose {computer_choice}! You win!\n")
        player_wins += 1
        print_standings()
        keep_going = input("Do you want to keep playing? Enter y to play again. ")
        if keep_going.lower() == "y":
            continue
        else:
            break
    elif player_choice == "scissors" and computer_choice == "rock":
        print(scissors_art)
        print("\nIt's scissors versus...\n")
        sleep(2)
        print(rock_art)
        print(f"\nComputer chose {computer_choice}! You lose!\n")
        computer_wins += 1
        print_standings()
        keep_going = input("Do you want to keep playing? Enter y to play again. ")
        if keep_going.lower() == "y":
            continue
        else:
            break
    elif player_choice == "scissors" and computer_choice == "paper":
        print(scissors_art)
        print("\nIt's scissors versus...\n")
        sleep(2)
        print(paper_art)
        print(f"\nComputer chose {computer_choice}! You win!\n")
        player_wins += 1
        print_standings()
        keep_going = input("Do you want to keep playing? Enter y to play again. ")
        if keep_going.lower() == "y":
            continue
        else:
            break
    elif player_choice == "paper" and computer_choice == "scissors":
        print(paper_art)
        print("\nIt's paper versus...\n")
        sleep(2)
        print(scissors_art)
        print(f"\nComputer chose {computer_choice}! You lose!\n")
        computer_wins += 1
        print_standings()
        keep_going = input("Do you want to keep playing? Enter y to play again. ")
        if keep_going.lower() == "y":
            continue
        else:
            break
    elif player_choice == "paper" and computer_choice == "rock":
        print(paper_art)
        print("\nIt's paper versus...\n")
        sleep(2)
        print(rock_art)
        print(f"\nComputer chose {computer_choice}! You win!\n")
        player_wins += 1
        print_standings()
        keep_going = input("Do you want to keep playing? Enter y to play again. ")
        if keep_going.lower() == "y":
            continue
        else:
            break
