# import modules
import random
from time import sleep

# random option
options = ["Rock", "Paper", "Scissors"]


# define the startup interaction
def startup():
    print("Be ready to choose between Rock, Paper and Scissors!")
    for sec in range(1, 4):
        sleep(1)
        print(sec)


# check the statements
def check_outcomes():
    player = input("Enter your choice: ")
    computer = random.choice(options)

    if player == computer:
        print(f"Computer chose {computer}!")
        print("It's a tie!")
        exit()
    elif player == "Rock":
        if computer == "Paper":
            print(f"Computer chose {computer}!")
            print(f"{computer} beats the {player}! Computer won!")
            exit()
        else:
            print(f"Computer chose {computer}!")
            print(f"{player} beats the {computer}! You won!")
            exit()
    elif player == "Paper":
        if computer == "Scissors":
            print(f"Computer chose {computer}!")
            print(f"{computer} beats the {player}! Computer won!")
            exit()
        else:
            print(f"Computer chose {computer}!")
            print(f"{player} beats the {computer}! You won!")
            exit()
    elif player == "Scissors":
        if computer == "Rock":
            print(f"Computer chose {computer}!")
            print(f"{computer} beats the {player}! Computer won!")
            exit()
        else:
            print(f"Computer chose {computer}!")
            print(f"{player} beats the {computer}! You won!")
            exit()
    else:
        print("Sorry! You've entered invalid name!")
        exit()


# gameplay
while True:
    startup()
    check_outcomes()
