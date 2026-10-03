# "import" va chercher une boîte à outils (un "module") rangée à part.
# La boîte "random" (= "hasard" en anglais) sert à faire des choix
# au hasard. On s'en servira pour que l'ordinateur choisisse son coup.
import random


# ---------------------------------------------------------------------
# ÉTAPE 2 : Demander le nombre de manches à gagner
# ---------------------------------------------------------------------
# On lit cette ligne de l'INTÉRIEUR vers l'EXTÉRIEUR :
#   1) input("...") affiche la question et attend que l'utilisateur
#      tape une réponse puis appuie sur Entrée.
#   2) int(...) transforme cette réponse en NOMBRE ENTIER.
#      Pourquoi ? Parce que input() renvoie toujours du TEXTE :
#      si on tape 3, Python reçoit le texte "3", pas le nombre 3.
#      Or on ne peut pas faire de calculs avec du texte.
#   3) manches = ... range le résultat dans une VARIABLE nommée "manches".
#
# Une variable, c'est une BOÎTE avec une ÉTIQUETTE : le nom est écrit
# sur l'étiquette, et la valeur est rangée dedans.
# Attention : en Python, "=" ne veut pas dire "égal" mais "RANGE DANS".
manches = int(input("Combien de manches voulez-vous jouer ? "))


# ---------------------------------------------------------------------
# ÉTAPE 3 : Préparer les scores
# ---------------------------------------------------------------------
# On crée deux boîtes pour compter les points.
# Au début, personne n'a encore gagné de manche : on met 0 partout.
score_joueur = 0
score_ordi = 0


# ---------------------------------------------------------------------
# ÉTAPE 4 : La liste des coups possibles
# ---------------------------------------------------------------------
# Les parenthèses créent un "tuple" : une liste FIGÉE (non modifiable).
# Les guillemets indiquent que "P", "F" et "C" sont du TEXTE.
#
# Chaque élément a une POSITION, et en informatique on compte À PARTIR DE 0 :
#
#     Position :    0        1         2
#     Coup     :   "P"      "F"       "C"
#                 Pierre   Feuille   Ciseaux
#
# Retiens bien cet ordre, il sert à l'étape 9 !
options = ("P", "F", "C")


# ---------------------------------------------------------------------
# ÉTAPE 5 : La boucle principale - on joue des manches en boucle
# ---------------------------------------------------------------------
# "while" veut dire "TANT QUE". Tout le bloc DÉCALÉ en dessous va se
# RÉPÉTER encore et encore, tant que la condition est vraie.
#
# La condition se lit :
#   "Tant que le score du joueur est PLUS PETIT QUE le nombre de manches
#    ET que le score de l'ordi est PLUS PETIT QUE le nombre de manches..."
# Autrement dit : tant que PERSONNE n'a encore gagné, on continue.
#
# Les deux-points ":" annoncent le début du bloc.
# Les lignes décalées de 4 espaces vers la droite font partie de la boucle.
# Ce décalage (l'"indentation") est OBLIGATOIRE en Python.
while score_joueur < manches and score_ordi < manches:

    # -----------------------------------------------------------------
    # ÉTAPE 6 : Le joueur fait son choix
    # -----------------------------------------------------------------
    # On pose la question et on range la réponse dans "choix_joueur".
    # .upper() transforme le texte en MAJUSCULES : si le joueur tape "p",
    # cela devient "P". Ainsi, minuscules et majuscules sont acceptées.
    choix_joueur = input("Que jouez-vous ? [P]ierre, [F]euille, [C]iseaux ").upper()

    # -----------------------------------------------------------------
    # ÉTAPE 7 : Vérifier que le choix est valide
    # -----------------------------------------------------------------
    # Et si le joueur tape "X" ou "banane" ? Il faut lui redemander !
    # Cette deuxième boucle se lit :
    #   "TANT QUE le choix du joueur ne fait PAS PARTIE des options,
    #    redemande-lui."
    #   - "in"     = "fait partie de"
    #   - "not in" = "ne fait PAS partie de"
    # Si le choix est bon dès le départ, on saute directement cette boucle.
    while choix_joueur not in options:
        choix_joueur = input("Choix valides : P F ou C ").upper()

    # -----------------------------------------------------------------
    # ÉTAPE 8 : L'ordinateur choisit au hasard
    # -----------------------------------------------------------------
    # On utilise la boîte à outils "random" chargée à l'étape 1.
    # random.choice(options) pioche UN élément au hasard dans la liste,
    # comme si on tirait un papier dans un chapeau.
    # Le point veut dire : "l'outil choice qui est dans la boîte random".
    choix_ordi = random.choice(options)

    # print() AFFICHE du texte à l'écran.
    # Les virgules séparent les morceaux ; Python met un espace entre eux.
    # Exemple d'affichage :  P x C
    print(choix_joueur, "x", choix_ordi)

    # -----------------------------------------------------------------
    # ÉTAPE 9 : Qui gagne la manche ?
    # -----------------------------------------------------------------
    # if   = "SI"
    # elif = "SINON SI"
    # else = "SINON" (tous les cas restants)
    # Python teste les cas DANS L'ORDRE et n'exécute que le PREMIER
    # qui est vrai.

    # --- Cas 1 : égalité ---
    # "==" (DEUX signes égal) pose la QUESTION "est-ce que c'est égal ?".
    # À ne pas confondre avec "=" (UN seul) qui sert à ranger dans une boîte.
    # Si les deux ont joué la même chose : égalité, aucun point marqué.
    if choix_joueur == choix_ordi:
        print("Égalité")

    # --- Cas 2 : le joueur gagne (la ligne la plus astucieuse !) ---
    # options.index(...) donne la POSITION d'un coup dans la liste.
    #   Exemple : options.index("F") donne 1.
    #
    # L'ASTUCE : dans la liste P, F, C, chaque coup BAT CELUI JUSTE AVANT LUI :
    #   - F (1) bat P (0)
    #   - C (2) bat F (1)
    #   - P (0) bat C (2)  <- ici on "fait le tour", comme sur une horloge
    # Donc : le joueur gagne si  sa position = position de l'ordi + 1.
    #
    # Le "% 3" (modulo) donne le RESTE de la division par 3.
    # Il gère le "tour d'horloge" :
    #   si l'ordi joue C (position 2) : 2 + 1 = 3, et 3 % 3 = 0 -> c'est P !
    #
    # Vérification de tous les cas gagnants :
    #   Joueur F, Ordi P :  1 == (0 + 1) % 3 = 1   -> oui
    #   Joueur C, Ordi F :  2 == (1 + 1) % 3 = 2   -> oui
    #   Joueur P, Ordi C :  0 == (2 + 1) % 3 = 0   -> oui
    elif options.index(choix_joueur) == (options.index(choix_ordi) + 1) % 3:
        # "+= 1" est un raccourci pour : score_joueur = score_joueur + 1
        # On prend le score actuel, on ajoute 1, et on le range au même endroit.
        score_joueur += 1
        print("Vous remportez la manche 👨‍💻")

    # --- Cas 3 : sinon, c'est l'ordinateur qui gagne ---
    # Ni égalité, ni victoire du joueur : il ne reste qu'une possibilité.
    # Pas besoin de vérifier, "else" attrape tous les cas restants.
    else:
        score_ordi += 1
        print("L'ordinateur remporte la manche 🤖")

    # -----------------------------------------------------------------
    # ÉTAPE 10 : Afficher le score de la manche
    # -----------------------------------------------------------------
    # Exemple d'affichage :  [ 2 - 1 ]
    # C'est la DERNIÈRE ligne décalée, donc la fin de la boucle.
    # Ensuite, Python REMONTE au "while" de l'étape 5 et revérifie
    # la condition. Si personne n'a gagné, une nouvelle manche commence.
    print("[", score_joueur, "-", score_ordi, "]")


# ---------------------------------------------------------------------
# ÉTAPE 11 : Annoncer le vainqueur de la partie
# ---------------------------------------------------------------------
# Ces lignes ne sont PLUS décalées : elles sont EN DEHORS de la boucle.
# Elles ne s'exécutent qu'UNE SEULE FOIS, quand la boucle est terminée,
# c'est-à-dire quand l'un des deux joueurs a atteint le nombre de manches.
#
# Si le score du joueur est égal au nombre de manches, il a gagné.
# Sinon, c'est forcément l'ordinateur (la boucle ne s'arrête que si
# l'un des deux a atteint le but).
if score_joueur == manches:
    print("Vous avez gagné la partie ✅")
else:
    print("L'ordinateur gagne la partie ❌")