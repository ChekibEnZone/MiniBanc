# Séance 2 : 3 exercices Python (environ 30 min)
# Écris ton code sous chaque énoncé, puis lance avec le triangle ▶.
# Bloqué plus de 10 min ? Demande un indice plutôt que la solution.


# ======================================================================
# EXERCICE 1 : la fonction verdict, comme un sous-VI (environ 8 min)
# Tu apprends : def, paramètres, valeurs par défaut, return
# ======================================================================
# a) Écris une fonction verdict(tension, mini=3.0, maxi=3.6)
#    qui renvoie (return) "OK" si mini <= tension <= maxi, et "KO" sinon.
# b) Teste-la avec ces 4 lignes, puis vérifie les résultats attendus :
#    print(verdict(3.3))                   -> OK
#    print(verdict(4.1))                   -> KO
#    print(verdict(4.1, mini=4.0, maxi=4.5))  -> OK  (autres limites)
#    print(verdict(3.6))                   -> OK  (borne comprise)
# Bonus : ajoute une 3e réponse "HORS PLAGE" si la tension est négative
#         ou supérieure à 5.0 (mesure impossible = capteur en panne).



# ======================================================================
# EXERCICE 2 : la fiche de chaque carte avec des dictionnaires (environ 12 min)
# Tu apprends : dictionnaires, liste de dictionnaires, append, statistiques
# ======================================================================
mesures = [3.2, 3.5, 4.1, 2.9, 3.3, 3.6, 3.0, 5.0, 3.4, 3.1]

# a) Crée une liste vide : resultats = []
# b) Avec une boucle for, pour chaque mesure, crée un dictionnaire :
#       {"carte": numéro (1, 2, 3...), "tension": la mesure, "verdict": verdict(mesure)}
#    et ajoute-le à la liste avec resultats.append(...)
#    Indice pour le numéro : for numero, m in enumerate(mesures, start=1):
# c) Affiche une ligne par carte, par exemple :  Carte 3 : 4.1 V -> KO
# d) Calcule et affiche le bilan du lot :
#       nombre de OK, nombre de KO, rendement en %,
#       tension moyenne, tension mini, tension maxi
#    Résultat attendu : 7 OK, 3 KO, rendement 70.0 %
# Bonus : affiche la liste des numéros des cartes KO -> [3, 4, 8]



# ======================================================================
# EXERCICE 3 : le rapport de test daté (environ 10 min)
# Tu apprends : module csv, datetime, écrire un fichier
# ======================================================================
# a) En haut du fichier, ajoute :  import csv  et  from datetime import datetime
# b) Écris rapport.csv avec une ligne d'en-tête : date ; carte ; tension ; verdict
#    puis une ligne par carte de ta liste resultats.
#    Indice :
#       with open("rapport.csv", "w", newline="") as f:
#           ecrivain = csv.writer(f, delimiter=";")
#           ecrivain.writerow(["date", "carte", "tension", "verdict"])
#    La date du jour : datetime.now().strftime("%d/%m/%Y %H:%M:%S")
# (La relecture du fichier avec try/except, ce sera pour la séance 3.)
# Bonus : ouvre rapport.csv dans Excel. Le ; permet à Excel (en français)
#         de bien séparer les colonnes.


# Etape 1 : Ecrire une fonction

def verdict (tension):
    if 3.0 <= tension <= 3.6 :
        return  "OK"
    else :
        return "NOK"
    
print(verdict(3.3))
print(verdict(4.1))

def verdict (tension, mini=3.0, maxi=3.6):
    if mini <= tension <= maxi :
        return "OK"
    else :
        return "NOK"

print (verdict(3.3))
print (verdict (4.1))
print(verdict(4.1, mini = 4, maxi = 4.5))
 

  # Exercice 2 : 
  
carte = {"numero": 1, "tension": 3.2, "verdict": "OK"}
print(carte["tension"])
print(carte["verdict"])

mesures=[3.2, 3.5, 4.1, 2.9, 3.3, 3.6, 3, 5.0, 3.4, 3.1 ]

resultat = []

numero = 1

for m in mesures:
    fiche = {"numero": numero, "tension" : m, "verdict": verdict(m)}
    resultat.append(fiche)
    numero= numero +1

    for fiche in resultat :
     print ("carte", fiche["numero"], ":", fiche["tension"], "V ---", fiche["verdict"])
        


#Etape 3 : le bilan du lot 

nb_ok = 0
nb_nok = 0

for fiche in resultat : 
    if fiche["verdict"] == "OK" :
        nb_ok = nb_ok + 1
    else  :
        nb_nok = nb_nok + 1


rendement = nb_ok / (nb_ok + nb_nok) * 100
print("OK :", nb_ok)
print("NOK :", nb_nok)
print("Rendement : ", rendement, "%")


#Exercice 3 : Ecrire le fichier

import csv
from datetime import datetime

#Etape 2 : écrire le fichier : 

maintenant = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

with open ("rapport.csv", "w", newline="")as f:
    ecrivain = csv.writer(f, delimiter=";")
    ecrivain.writerow(["date","carte","tension", "verdict" ])
    for fiche in resultat : 
        ecrivain.writerow([maintenant, fiche["numero"], fiche["tension"], fiche["verdict"]])

    print("Rapport écrit !")