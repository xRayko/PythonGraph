import random
Valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'Roi':10 , 'Dame':10, 'Valet':10 }

tirageGroupier = random.choice(list(Valeurs.keys()))
tirageJoueur = random.choice(list(Valeurs.keys()))
tirageJoueur2 = random.choice(list(Valeurs.keys()))
ListCartJoueur =[ tirageJoueur, tirageJoueur2]
ListCartCroupier =[ tirageGroupier]

resultat = Valeurs[ListCartJoueur[0]] + Valeurs[ListCartJoueur[1]]
résultatCroupier = Valeurs[ListCartCroupier[0]]

print(f"Le groupier a tiré un {tirageGroupier}")
print(f"Le joueur a tiré un {tirageJoueur}")
print(f"Le joueur a tiré un {tirageJoueur2}")
print( resultat)

choix = "o"
while resultat < 21 and choix == "o":
    choix = input("Voulez-vous tirer une carte ? (o/n) ")
    if choix == "o":
        tirageJoueur3 = random.choice(list(Valeurs.keys()))
        ListCartJoueur.append(tirageJoueur3)
        print(f"Le joueur a tiré un {tirageJoueur3}")
        resultat = resultat + Valeurs[tirageJoueur3]
        print(resultat)
if resultat < 22:
    while résultatCroupier < 17 :
        tirageCroupier2 = random.choice(list(Valeurs.keys()))
        ListCartCroupier.append(tirageCroupier2)
        print(f"Le croupier a tiré un {tirageCroupier2}")
        résultatCroupier = résultatCroupier + Valeurs[tirageCroupier2]
        print(résultatCroupier)
    if résultatCroupier < 22 and résultatCroupier> resultat:
        print("Groupier Win")
    elif résultatCroupier == resultat:
        print("Egalité")
    else:
        print("Joueur Win")
else: print("PErdu ")