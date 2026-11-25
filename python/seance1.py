# Séance 1 : premiers pas en Python
# Pour lancer ce fichier : clique sur le triangle ▶ en haut à droite de VS Code.
# Les lignes qui commencent par # sont des commentaires : Python les ignore.

# --- Étape 1 : afficher un message ---

tension = 3.8
print(tension)

# --- Etape 3: les types

nb_cartes = 12 
nom_banc = "Mini banc 1"
carte_ok = True

print(type(tension))
print(type(nom_banc))
print(type(carte_ok))

# Etape 4 : Les conditions

if tension >= 3.0 and tension  <= 3.6 :
    print("OK")
else:
    print("NOK")

 # Etape 5 : Les listes : 

mesures = [3.2, 3.5, 4.1, 2.9, 3.3]   

print(mesures)
print(mesures[0])
print(len(mesures))
print(max(mesures))


# Etape 6 : Boucle For :

for m in mesures : 
    if 3.0 <= m <= 3.6:
        print(m, "OK")
    else :
        print(m, "NOK")





