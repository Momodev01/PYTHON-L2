"""
Exercice 1-5 :
Écrire un algorithme qui lit les données d'un produit. Un produit est caractérisé par son 
libelle(chaine), sa quantité en stock(réel), le prix unitaire (réel).
L'algorithme affiche les informations du produit, puis calcule et affiche :
    ● Le montant en stock de chaque produit, MStock=prix unitaire * stock
    ● Le montant TTC, MTTC=MStock + MStock* TVA
    ● TVA=18%
"""

print("Entrer les informations d'un produit")
libelle = input("Libellé: ")
qteStock = float(input("La quantité en stock: "))
prixUnitaire = float(input("Le prix unitaire: "))
TVA = 18/100
MStock = prixUnitaire * qteStock
MTTC = MStock + (MStock * TVA)

print(
    "Le libellé du produit: ", libelle, '\n'
    "Sa Quantité en Stock: ", qteStock, '\n'
    "Son Prix Unitaire: ", prixUnitaire, '\n'
    "Son Montant en Stock: ", MStock, '\n'
    "Son Montant TTC: ", MTTC 
)
