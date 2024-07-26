"""
Exercice 1-6 :
Écrire un algorithme qui lit les données d'un étudiant. Un étudiant est caractérisé par son 
nom(chaîne),prénom (chaîne),date de naissance (j/mois/annel).L'algorithme affiche les 
informations de l'étudiant ,puis calcule et affiche l'âge. L’année en cours est considérée 
comme une constante.
"""
import datetime
print("Entrer les informations d'un étudiant")
nom = input("Nom: ")
prenom = input("Prenom: ")
naissance = input("La date de naissance en jj/mm/aaaa: ")
anneeEnCours = 2024
# age = anneeEnCours - int(naissance[6:10])
t = datetime.datetime.strptime(naissance, "%d-%m-%Y")

print("L'étudiant est: ", nom, prenom, "né le", t)

# print(
#     "Le nom de l'étudaint: ", nom, '\n'
#     "Son Prénom: ", prenom, '\n'
#     "Son âge: ", age
# )
