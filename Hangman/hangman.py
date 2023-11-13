import os
import random
import sys

WORDS_FILE = "slownik.txt"


def load_words():
    print("Loading words...")
    try:
        path_words = os.path.join(os.getcwd(), "Hangman", WORDS_FILE)

        with open(path_words, "r", encoding="utf-8") as f:
            words_list = f.read().split()
    except:
        print(
            "Words loading error ! \n \
              Exiting the game..."
        )
        sys.exit()
    else:
        print("Words loaded succesfully!")
        return words_list


def choose_word(words_list):
    return random.choice(words_list)


def is_word_guessed(word, letters_guessed):
    if set(word).issubset(set(letters_guessed)):
        return True
    else:
        return False


def guessed(word, letters_guessed):
    guessed = []
    for letter in word:
        if letter in letters_guessed:
            guessed.append(letter)
        else:
            guessed.append("_")
    return "".join(guessed)


def hangman(words):
    word = choose_word(words).lower()

    letters_guessed = []
    tries = 11

    print("\nHello in Hangman game, where you have 11 tries to guess hidden word. \n")
    print(f"Word that I am thinking about is {len(word)} letters long.")

    while tries > 0:
        if is_word_guessed(word, letters_guessed):
            print("\nCongratulations, you win!")
            break
        else:
            print(f"\nRemaining tries: {tries} \n")
            letter = input("Enter a letter: ").lower()
            if letter in letters_guessed:
                print("This letter was already guessed!")
                print(f"Guessed: {guessed(word,letters_guessed)}")
            elif letter in word:
                letters_guessed.append(letter)
                print("Nice! You guessed a letter!")
                print(f"Guessed: {guessed(word,letters_guessed)}")

            else:
                letters_guessed.append(letter)
                tries -= 1
                print("Oops! This letter is not in the word...")
                print(f"Guessed: {guessed(word,letters_guessed)}")

        if tries == 0:
            print("\nYou lose :( You ran out of guesses...")
            print(f"The word was: {word}")
        else:
            continue


if __name__ == "__main__":
    words = load_words()

    while True:
        hangman(words)

        decision = input("Do you want to start a new game? If no enter N/n: ")

        if decision in ["n", "N"]:
            print("Than you for playing this game.")
            break
