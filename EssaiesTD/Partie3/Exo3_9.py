"""
Écrire un programme qui permet de tester si deux nombres sont AMIS ou pas. 
Deux nombres M et N sont amis si la somme des diviseurs de N excepté 1 et lui-même est 
égale à M et la somme des diviseurs de M excepté 1 et lui-même est égale à N.
Exemple: les nombres 48 et 75 sont deux nombres amis puisque :
Les diviseurs de 48 sont: 2, 3, 4, 6, 8, 12, 16, 24 => 2 + 3 + 4 + 6 + 8 + 12 + 16 + 24 = 75
Les diviseurs de 75 sont : 3, 5, 15, 25 => 3 + 5 + 15 + 25 = 48

"""

# Saisir deux nombres entiers
M = int(input("Entrez le premier nombre: "))
# Chercher les diviseurs de chaque nombre
def diviseurs(n):
    div = [i for i in range(2, n) if n % i == 0]
    print (div)
           # Calculer la somme des diviseurs de chaque nombre
    # def somme_diviseurs(n):
    #     return sum(diviseurs(n))