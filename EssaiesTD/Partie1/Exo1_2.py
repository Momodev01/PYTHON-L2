"""
Exercice 1-2 : Écrire un programme qui demande à l'utilisateur de donner valeur d'une 
monnaie en CFA, puis détermine et affiche sa correspondance en DOLLAR $ et en LIVRE 
STERLING £.
"""

cfa = int(input("Entrez une valeur de monnaie en CFA: "))
dollar =  cfa * 0.0016
gbp = cfa * 0.0012
euro = cfa * 0.0013

print(
    "La valeur en Dollar est: ", dollar, "$\n"
    "La valeur en Livre Sterling est: ", gbp, "£\n"
    "La valeur en Euro est: ", euro, "€"
)
