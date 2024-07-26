"""
Exercice 1-3 : Écrire un programme qui demande à l’utilisateur de donner la longueur et la 
largeur d’un rectangle et lui retourne son périmètre, sa surface et la longueur d’un des 
diagonales.
"""

from math import sqrt

longueur = int(input("Entrer la longueur du rectangle: "))
largeur = int(input("Entrer la largeur du rectangle: "))

perimetre = 2 * (longueur + largeur)
surface = longueur * largeur
diagonale = ((longueur**2) + (largeur**2)) ** (1/2)



print(
    "Le périmètre du rectangle vaut:", perimetre, "\n"
    "Le surface du rectangle vaut:", surface, "\n"
    "Le diagonale du rectangle vaut:", diagonale 
)