#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt
import os

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("Seance-02/Exercice/src/data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)

# Mettre dans un commentaire le numéro de la question
# Question 1
print(contenu)

# Question 2
print(len(contenu.columns)) # Nombre de colonnes
print(len(contenu)) # Nombre de lignes

# Question 3
print(contenu.dtypes) # type de chaque colonne

# Question 4
print(contenu.columns) # noms des colonnes

# Question 5
print(contenu['Inscrits'].head(len(contenu))) #nombre des inscrits

# Question 6
quantitative_sums=[]

for colonne in contenu.columns:

    if contenu[colonne].dtype == 'int64' or contenu[colonne].dtype == 'float64':
        sum_colonne = contenu[colonne].sum()
        quantitative_sums.append((colonne, sum_colonne))

print("\n")
print("Sommes des colonnes quantitatives:")
for nom, somme in quantitative_sums:
    print(nom, ": ", somme)

# Question 7  

departements = contenu.groupby('Code du departement')[['Inscrits', 'Votants']].sum().reset_index() # Agrégation des données par département

for index, row in departements.iterrows():
    code = row['Code du departement']   
    inscrits = row['Inscrits']
    votants = pd.to_numeric(row['Votants'], errors='coerce') #parceque certains valeurs sont des strings
  
    data = [inscrits, votants]
    labels = ['Inscrits', 'Votants']
    plt.figure(figsize=(6, 4))
    plt.bar(labels, data, color=["blue", "orange"])
    plt.title(f"Département {code}: Inscrits vs Votants")
    plt.ylabel("Nombre")
    
    image = os.path.join("Seance-02/Exercice/src/data", f"dept{code}_inscrits_votants.png")
    plt.savefig(image)
    plt.close()

# Question 8
departements = contenu.groupby('Code du departement')[['Abstentions', 'Blancs','Nuls', 'Exprimés']].sum().reset_index() # Agrégation des données par département

for index, row in departements.iterrows():
    code = row['Code du departement']   
    abstentions = row['Abstentions']
    blancs=row['Blancs']
    nuls=row['Nuls']
    experimes = pd.to_numeric(row['Exprimés'], errors='coerce') #parceque certains valeurs sont des strings
  
    data = [abstentions, blancs, nuls, experimes]
    labels = ['Abstentions','Blancs','Nuls', 'Exprimés']
    plt.figure(figsize=(7, 7))
    plt.pie(data,labels=labels, 
            autopct='%1.1f%%',
            startangle=90) 
    plt.title(f"Département {code}: Vote et Abstention")
    plt.axis('equal')
    
    image1 = os.path.join("Seance-02/Exercice/src/data", f"dept{code}_vote_et_abst.png")
    plt.savefig(image1)
    plt.close()

# Question 9
inscrits_data = contenu['Inscrits'].loc[contenu['Inscrits'] > 0]
plt.figure(figsize=(9, 6))
plt.hist(inscrits_data, bins=30, color='green', edgecolor='black',density=True)
plt.title("Histogramme de la distribution des Inscrits")
plt.xlabel("Nombre d'Inscrits (par bureau de vote)")
plt.ylabel("Densité de Probabilité")
plt.grid(axis='y', alpha=0.5)

hist = os.path.join("Seance-02/Exercice/src/data", "hist.png")
plt.savefig(hist)
plt.close()