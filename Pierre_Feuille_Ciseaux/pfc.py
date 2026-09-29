import random

manches = int(input("Combien de manches voulez-vous jouer ? "))

score_joueur = 0
score_ordi = 0

options = ("P", "F", "C")

while score_joueur < manches and score_ordi < manches:
    choix_joueur = input("Que jouez-vous ? [P]ierre, [F]euille, [C]iseaux ").upper()

    while choix_joueur not in options:
        choix_joueur = input("Choix valides : P F ou C ").upper()

    choix_ordi = random.choice(options)

    print(choix_joueur, "x", choix_ordi)

    if choix_joueur == choix_ordi:
        print("Égalité")
    elif options.index(choix_joueur) == (options.index(choix_ordi) + 1) % 3:
        score_joueur += 1
        print("Vous remportez la manche 👨‍💻")
    else:
        score_ordi += 1
        print("L'ordinateur remporte la manche 🤖")

    print("[", score_joueur, "-", score_ordi, "]")

if score_joueur == manches:
    print("Vous avez gagné la partie ✅")
else:
    print("L'ordinateur gagne la partie ❌")