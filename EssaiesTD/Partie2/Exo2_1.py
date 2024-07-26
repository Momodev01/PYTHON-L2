# Partie 2 : Structures Conditionnelles

"""
Exercice 2-1 : Écrire un algorithme calculatrice permettant la saisie du premier entier (a) de 
l'opération ( + ou - ou * ou / : sont des caractères) et du deuxième entier (b) et qui affiche le 
résultat.
"""

try:
    a = int(input("Saisir un entier \t"))
    b = int(input("Saisir un autre \t"))
    op = input("Choisir un opérateur\t")
    
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a/b)
except Exception as e:
    print("Erreur")


# print("Rest ", 9, sep = "/")
# i=1
# while(i<10):
#     print(i,end="-")
#     i=i+1