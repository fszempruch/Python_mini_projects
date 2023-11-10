### Hangman

import more_itertools

print("Witaj w grze WISIELEC, w której masz 11 prób aby odgadnąć zagadkowe słowo ! \n")
word = input("Podaj słowo do odgadnięcia przez drugą osobę: ").upper()
len_word = len(word)
print(f"Słowo jest {len_word} literowe!")

litery = set(word)
wykorzystane_litery = []

odgadniete = list("_" * len_word)
proby = 11

while True:
    print("Liczba pozostałych prób: ", proby)
    litera = input("Podaj literę: ").upper()

    while litera in wykorzystane_litery:
        print("Ta litera juz była wykorzystana!")
        litera = input("Podaj literę: ").upper()

    if litera in litery:
        print("Brawo, trafiłeś literę!")
        wykorzystane_litery.append(litera)
        if litera in litery:
            indeksy_liter = list(more_itertools.locate(word, lambda x: x == litera))
            for i in indeksy_liter:
                odgadniete[int(i)] = litera
            print("".join(odgadniete))
            if "".join(odgadniete) == word:
                print("WYGRANA!")
                break
    else:
        print("Przykro mi, nie trafiłeś litery...")
        proby -= 1

    if proby == 0:
        print("PRZEGRANA...")
        break
