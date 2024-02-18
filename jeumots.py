import random

with open('liste_francais.txt', 'r', encoding='utf-8') as file:
    liste_francais = file.read().splitlines()

word = random.choice(liste_francais).upper()
length = len(word)

GREEN = "\u001b[32;1m"
RED = "\u001b[31;1m"
YELLOW = "\u001b[33;1m"
RESET = "\u001b[0m"

# https://www.freelang.com/dictionnaire/dic-francais.php

print("Mot de longueur :",length)

num_try = 5

for i in range (num_try) :
    guess = input("Tapez votre réponse : ").upper()
    if(len(guess)!=length):
        print("Veuillez écrire un mot de",length,"lettres")
    else:
        for i in range(0,length):
            if guess[i] == word[i]:
                print(f"{GREEN}{guess[i]}{RESET}", end="")
            elif guess[i] in word:
                print(f"{YELLOW}{guess[i]}{RESET}", end="")
            else:
                print(f"{RED}{guess[i]}{RESET}", end="")
        print()

        if guess == word :
            print("Vous avez gagné !")
            break;

print("Vous avez perdu, le mot était",word)