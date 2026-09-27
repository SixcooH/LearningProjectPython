case_vide = " " #ici on crée une variable qui repésente une case 

plateau = [case_vide for i in range(9)] #suite de 0 a 8 de case vide

symboles = ("❌", "⭕") #contient les pions des deux joueurs 
placeholder = ("1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ ", "9️⃣ ") #contient les chiffres affichés dans les cases vides, pour savoir quel numéro taper

joueur = symboles[0]#position 0

def afficher_plateau(): #def: sert a créer, un bloc de code ou l'on donne un nom pour le réutiliser 
    print(" ----+----+----") #print affiche du texte a l'écran, ici il sera en haut de la grille 
    for i in range(9): #boucle for qui répète le code en dessous 9 fois et sur chaque tour la variable i prend la valeur suivante
        print("|", plateau[i] if plateau[i] != case_vide else placeholder[i], end=" ") #ici on lit "affiche plateau[i] si la case n'est pas vide (!= veut dire différent de) sinon placeholder[i]"
        if i % 3 == 2: #si la case contient x ou o on affiche, si c'est vide on affiche les numéros
            print("|")
            print(" ----+----+----")


while True:
    afficher_plateau()
    choix_joueur = 0

    while choix_joueur < 1 or choix_joueur > 9 or plateau[choix_joueur - 1] != case_vide:
        choix_joueur = int(input("Entrez une case entre 1 et 9 : "))

    plateau[choix_joueur - 1] = joueur

    if case_vide != plateau[0] == plateau[1] == plateau[2] \
    or case_vide != plateau[3] == plateau[4] == plateau[5] \
    or case_vide != plateau[6] == plateau[7] == plateau[8] \
    or case_vide != plateau[0] == plateau[3] == plateau[6] \
    or case_vide != plateau[1] == plateau[4] == plateau[7] \
    or case_vide != plateau[2] == plateau[5] == plateau[8] \
    or case_vide != plateau[0] == plateau[4] == plateau[8] \
    or case_vide != plateau[2] == plateau[4] == plateau[6]:
        print("Le joueur", joueur, "gagne la partie !")
        afficher_plateau()
        break

    joueur = symboles[1] if joueur == symboles[0] else symboles[0]