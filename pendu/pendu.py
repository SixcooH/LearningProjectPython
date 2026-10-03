HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



mot_mystere = "commentcoder"
mot_miniscule = mot_mystere.lower()
mot_visible = ["*"] * len(mot_mystere)
nb_vies = 7

while True:
    print("Mot :", "".join(mot_visible))
    print("Nombre de vies :", nb_vies)

    lettre = ""
    while len(lettre) != 1 or not lettre.isalpha():
        lettre = input("Entrez une lettre : ").lower()

    if lettre in mot_miniscule:
        for i, char in enumerate(mot_miniscule):
            if char == lettre:
                mot_visible[i] = lettre
    else:
        nb_vies -= 1

    if mot_miniscule == "".join(mot_visible):
        print("Vous avez gagné ! 🎉")
        break
    elif nb_vies == 0:
        print("Vous avez perdu ! ❌ Le mot était :", mot_mystere)
        break
    else:
        print(HANGMANPICS[7 - nb_vies])