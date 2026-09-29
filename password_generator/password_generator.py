import random #module python pour tirer au hasard (tirer un élément au sort, mélanger une liste..)
import string #module pyhton contient des listes de caractères déja écrites 
#on accède au contenu via random. ou string.

def generer_mot_de_passe(longueur): #fonction qui tient un paramètre longueur qui contiendra la valeur du nombre de caractères dans le mdp
    if longueur < 4: #4 caractères minimum sinon avertissement print
        print("La longueur doit être d'au moins 4.")
        return "" #il arrête la fonction immédiatement et renvoie vide

    minuscule = random.choice(string.ascii_lowercase) #appel les modules 
    majuscule = random.choice(string.ascii_uppercase)
    chiffre = random.choice(string.digits)
    symbole = random.choice(string.punctuation)

    tous_les_caracteres = string.ascii_letters + string.digits + string.punctuation
    reste = [random.choice(tous_les_caracteres) for _ in range(longueur - 4)]

    mot_de_passe_liste = [minuscule, majuscule, chiffre, symbole] + reste
    random.shuffle(mot_de_passe_liste)

    return "".join(mot_de_passe_liste)


if __name__ == '__main__':
    longueur = int(input("Longueur du mot de passe : "))
    mot_de_passe = generer_mot_de_passe(longueur)

    if mot_de_passe != "":
        print("Mot de passe généré :", mot_de_passe)