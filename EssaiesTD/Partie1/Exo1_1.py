"""
Exercice 1-1 : Écrire un programme qui saisit deux entiers a et b, calcule et affiche le 
quotient entier, le reste de la division, le ratio (quotient réel) et modulo.
"""

a = int(input("Saisissez un entier: "))
b = int(input("Saisissez un autre: "))
print(
    "Le quotient entier est: ", a//b ,"\n"
    "Le reste est: ", a%b ,"\n"
    "Le quotient réel est: ", a/b ,"\n"
    "Le modulo est: ", a%b
)

# print("Le reste est: ", a%b)
# print("Le quotient réel est: ", a/b)
# print("Le modulo est: ", a%b)
