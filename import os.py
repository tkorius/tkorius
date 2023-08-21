import os
from random import randrange
from math import ceil
argent = 1000
continuer_partie = True

print("vous vous installez a la table de roulette avec", argent,"$.")

while continuer_partie:
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Tapez le nombre sur lequel vous voulez vous voulez miser (entre 0 et 49):")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("vous n'avez pas saisi de nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Ce nombre est negatif")
            if nombre_mise > 49:
                print("Ce nombre est superieur a 49")
        mise = 0
        while mise <= 0 or mise > argent:
            mise = input("Tapez le montant de mise : ")
            try:
                mise = int(mise)
            except ValueError:
                print("Vous n'avez pas saisi de nombre")
                mise = -1
                continue
            if mise <= 0:
                print("La mise saisie est negatif ou nulle.")
            if mise > argent:
                print("Vous ne pouvez miser autant, vous n'avez que", argent,"$")
        numero_gagnant = randrange(50)
        print("La roulette tourne ... ... et s'arrete sur le numero", numero_gagnant)
        if numero_gagnant == nombre_mise:
            print("Felicitation ! Vous obtenez", mise * 3,"$ !")
            argent += mise * 3
        elif numero_gagnant % 2 == nombre_mise % 2:
            mise = ceil(mise * 0.5)
            print("Vous avez mise sur la bonne couleur. Vous obtenez",mise, "$")
            argent += mise
        else:
            print("Desole l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
            argent -= mise
        if argent <= 0:
            print("Vous etes ruine ! C'est la fin de la partie.")
            continuer_partie = False
        else:
            print("Vous avez a present",argent,"$")
            quitter = input("Souhaitez-vous quitter le casino (o/n) ?")
            if quitter == "o" or quitter == "O":
                print("Vous quittez le casino avec vos gains.")
                continuer_partie = False
os.system("pause")

