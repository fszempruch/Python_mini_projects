import random
import sys


def choice(selection):
    if selection == "1" or selection.lower() == "rock":
        return "rock"
    elif selection == "2" or selection.lower() == "scissors":
        return "scissors"
    elif selection == "3" or selection.lower() == "paper":
        return "paper"


def comparison(player, computer):
    if player == computer:
        return "Tie"
    elif (
        (player == "paper" and computer == "rock")
        or (player == "rock" and computer == "scissors")
        or (player == "scissors" and computer == "paper")
    ):
        return "You win"
    else:
        return "Computer wins"


def decision_get_and_validate():
    while True:
        decision = input().lower()
        if decision in ["e", "exit"]:
            print("Thank you for playing this game!")
            sys.exit()
        elif decision not in ["1", "2", "3", "rock", "scissors", "paper", "e", "exit"]:
            print("Wrong input, please try again...")
        else:
            return decision


def game():
    victories_counter = 0

    print("Hello in Rock, Scissors, Paper Game!")

    while True:
        print(" ")
        print("Victory counter: ", victories_counter)
        print(" ")
        print(
            "What do you choose: \n \
            1. Rock \n \
            2. Scissors \n \
            3. Paper \n \
            exit or e - for exit"
        )

        decision = decision_get_and_validate()

        player_choice = choice(decision)
        print("Your choice:", player_choice)

        computer_choice = choice(random.choice(["1", "2", "3"]))
        print("Computer's choice:", computer_choice)

        result = comparison(player_choice, computer_choice)

        print(result)

        if result == "You win":
            victories_counter += 1


if __name__ == "__main__":
    game()
