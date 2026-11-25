# MiniBanc

Mon mini-banc d'essai maison (PC + Arduino), le projet fil rouge de mon plan de formation en LabVIEW et en Python.

## LabVIEW

| Fichier | Description |
|---|---|
| `Test_simu_banc.vi` | Banc simulé : tension aléatoire 0-5 V, graphe déroulant, verdict OK/KO (3,0-3,6 V) et compteur de cartes OK (registre à décalage). |
| `Temp_Sensor_test.vi` | Test de capteur de température. |

## Python (`python/`)

Le même banc, réécrit en Python pour apprendre le langage.

### Séance 1 : les bases (`seance1.py`)
- Afficher un message avec `print`
- Variables et types : `float` (tension), `int` (nombre de cartes), `str` (nom du banc), `bool` (carte OK)
- Conditions `if / else` : verdict OK/NOK d'une tension entre 3,0 et 3,6 V
- Listes : une série de mesures, accès par position, `len()`, `max()`
- Boucle `for` : verdict automatique de chaque mesure de la liste

### Séance 2 : un banc de test complet (`seance2.py`)
1. **Fonction `verdict(tension, mini=3.0, maxi=3.6)`**, l'équivalent d'un sous-VI : les limites de test sont réglables, avec des valeurs par défaut.
2. **Une fiche par carte** : chaque carte testée devient un dictionnaire `{numero, tension, verdict}`, rangé dans une liste de résultats.
3. **Bilan du lot** : nombre de cartes OK et NOK, et rendement en % (7 OK, 3 NOK, 70 %).
4. **Rapport de test daté** : écriture d'un fichier CSV (séparateur `;` pour Excel) avec la date, le numéro de carte, la tension et le verdict. Exemple de sortie : `rapport_exemple.csv`.

| Notion Python | Équivalent LabVIEW |
|---|---|
| fonction `def` | sous-VI |
| liste | tableau |
| dictionnaire | cluster |
| boucle `for` | boucle For avec auto-indexation |
| compteur `n = n + 1` | registre à décalage |

## Outils

- LabVIEW 2026 Community Edition
- Digilent LINX (pilotage Arduino)
- Python 3.13, VS Code
