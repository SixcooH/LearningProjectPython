import random

manches = int(input("Combien de manches voulez-vous jouer ? "))

score_joueur = 0
score_ordi = 0

options = ("P", "F", "C")

while score_joueur < manches and score_ordi < manches:
    choix_joueur = input("Que jouez-vous ? [P]ierre, [F]euille, [C]iseaux ").upper()

    while choix_joueur not in options:
        choix_joueur = input("Choix valides : P F ou C ").upper()