import random


def choice(selection):
    if selection == "1" or selection.lower == "rock":
        return "rock"
    elif selection == "2" or selection.lower == "scissors":
        return "scissors"
    elif selection == "3" or selection.lower == "paper":
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


if __name__ == "__main__":
    possibilities = ["rock", "scissors", "paper"]

    print("Hello in Rock Scissors Paper Game!")

    victory_counter = 0

    while True:
        print("Victory counter: ", victory_counter)
        print(
            "What do you choose: \n \
            1. Rock \n \
            2. Scissors \n \
            3. Paper \n \
            exit or e - for exit"
        )

        decision = input().lower()

        if decision not in ["1", "2", "3", "rock", "scissors", "paper", "e", "exit"]:
            print("Wrong input, please try again...")
        elif decision in ["e", "exit"]:
            print("Thank you for playing this game!")
            print("Your result:", victory_counter)
            break
        else:
            player_choice = choice(decision)
            print("Your choice:", player_choice)

            computer_choice = random.choice(possibilities)
            print("Computer's coice:", computer_choice)

            result = comparison(player_choice, computer_choice)
            print(result)

            if result == "You win":
                victory_counter += 1
