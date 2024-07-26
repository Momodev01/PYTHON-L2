"""
Exercice 2-2 : Écrire un algorithme permettant de résoudre une équation du premier degré ax + b = 0
"""

try:
    a = int(input("Entrez la valeur de a : "))
    b = int(input("Entrez la valeur de b : "))
    x = -b/a
    
    if a == 0:
        if b == 0:
            print("L'équation admet une infinité de solutions")
        else :
            print("L'équation n'admet pas de solution")
    else:
        print(a,"x +", b, " = 0", sep="")
        print(a,"x = ", -b, sep="")
        print("x = ", -b/a)
        # print("La solution de l'équation est x = ", x)
        
except Exception as e:
    print('Equation non resolvable')