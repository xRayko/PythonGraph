import random

tabme = 0
tabot = 0

while tabme !=3 and tabot !=3:
    choix = input(" fais ton choix : ")
    game = ["pierre", "feuille", "ciseau"]
    list = random.choice(game)
    if choix == "pierre" and list == "pierre":
         print("egalité")
    elif choix == "feuille" and list == "feuille":
         print("egalité")
    elif choix == "ciseau" and list == "ciseau":
        print("egalité")
    elif choix == "pierre" and list == "feuille":
        print("perdue !")
        tabot +=1
    elif choix == "pierre" and list == "ciseau":
        print("gagner !")
        tabme +=1
    elif choix == "feuille" and list == "pierre":
        print("gagner !")
        tabme += 1
    elif choix == "feuille" and list == "ciseau":
        print("perdue !")
        tabot += 1
    elif choix == "ciseau" and list == "pierre":
        print("perdue !")
        tabot += 1
    elif choix == "ciseau" and list == "feuille":
        print("gagner !")
        tabme += 1
    else :
        print("vous devez jouer un symbole")
    print(list)
    print(f"Votre score est de :{tabme}")
    print(f"Le score du bot est de : {tabot}")
if tabme == 3:
    print("Vous avez gagner la partie BRAVOOO 🏆!!!")
else:
    print("Vous avez perdu, le bot à gagner")







