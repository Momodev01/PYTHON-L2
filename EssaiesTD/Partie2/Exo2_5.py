"""
Exercice 2-5 : Faire un programme qui saisit une date (jour, mois et année) puis détermine 
et affiche la date qu'il faisait il y a N jours.N est saisi au clavier et est positif.
"""

"""
Saisir une date en jour mois et année (j-m-a)
Saisir un nombre de jour N, telque N >= 1 et N <= 30
Vérifier si le nombre de jours j est supérieur à l'entier N saisi
Si oui, faire j - N et afficher la date qu'il  il y a j-N jours
Si non, emprunter un mois (mois - 1) et ajouter 30 à j (j + 30)

 
 Si N < j
    Faire J --> j - N
    Afficher la date (J-m-a)
  Sinon Si N > j
    Faire M --> m - 1
          J --> (j + 30) - N
    Afficher la date (J-M-a)
  FinSi

"""