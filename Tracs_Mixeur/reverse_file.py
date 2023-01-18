import csv

# Ouvrir le fichier d'entrée en lecture
with open('transactions.csv', 'r') as input_file:
    # Lire le fichier avec csv.reader
    reader = csv.reader(input_file)
    # Inverser les lignes de la liste
    rows = list(reader)[::-1]

# Ouvrir le fichier de sortie en écriture
with open('output.csv', 'w') as output_file:
    # Écrire les lignes inversées dans le fichier de sortie
    writer = csv.writer(output_file)
    writer.writerows(rows)
