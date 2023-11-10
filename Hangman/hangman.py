### Hangman

import more_itertools

print("Witaj w grze WISIELEC, w której masz 11 prób aby odgadnąć zagadkowe słowo ! \n")
slowo = input("Podaj słowo do odgadnięcia przez drugą osobę: ").upper()
print(f"Słowo jest {len(slowo)} literowe!")
litery = set(slowo)
wykorzystane_litery = []

odgadniete = list("_" * len(slowo))
proba = 11

while proba > 0:
    print("Liczba pozostałych prób: ", proba)
    litera = input("Podaj literę: ").upper()

    while litera in wykorzystane_litery:
        print("Ta litera juz była wykorzystana!")
        litera = input("Podaj literę: ").upper()

    if litera in litery:
        print("Brawo, trafiłeś literę!")
        wykorzystane_litery.append(litera)
        if litera in litery:
            indeksy_liter = list(more_itertools.locate(slowo, lambda x: x == litera))
            for i in indeksy_liter:
                odgadniete[int(i)] = litera
            print("".join(odgadniete))
            if "".join(odgadniete) == slowo:
                print("WYGRANA!")
                break
    else:
        print("Przykro mi, nie trafiłeś litery...")
        proba -= 1

    if proba == 0:
        print("PRZEGRANA...")
