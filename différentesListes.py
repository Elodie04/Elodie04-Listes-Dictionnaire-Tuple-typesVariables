#Dictionnaire 
fruits = {
    "pomme":"rouge","banane":"jaune","orange":"orange"
}

#Ajout d'un nouveau fruit 
fruits["kiwi"] = "vert"

#Ajout d'une nouvelle valeur
couleur_banane = fruits["banane"]

#Ajout d'un nouveau fruit 
fruits["pomme"] = "vert"

#Suppression du fruit
del fruits["banane"]

#Affichage des cles du dictionnaire
print(fruits.keys())

# Autre exercice #

 #Utilisation de plusieurs types de variables
nom = "Elodie"
age = 29
taille = 1.69
est_etudiant = True

print(f"Je m'appelle {nom} j'ai {age} ans, je mesure {taille} et je suis {est_etudiant} !")
print(type(nom))
print(type(age))
print(type(taille))
print(type(est_etudiant))


#Liste
fruits = [
    "pomme","banane", "orange"
]

#Ajout d'un nouveau fruits
fruits.append ("kiwi")

#Suppression d'un fruit
fruits.remove ("orange")

#Changement de fruits du second élement de la liste par ananas
fruits[1] = "ananas"

#Affichage de la longueur de la liste
print("len.fruits")

#On trie les elements par ordre alphabéthique
fruits.sort()

#On réaffiche pour voir les changements
print(fruits)

# Autre exercice #

#Tuple
mon_tuple = (0, 2, 99, 45, 1, 77, 63, 41, 21)
tuple_croissant = tuple(sorted(mon_tuple)) #Pour trier dans l'ordre croissant
print(tuple_croissant)


