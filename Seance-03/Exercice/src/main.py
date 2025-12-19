#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

# Sources des données : production de M. Forriez, 2016-2023

with open("Seance-02/Exercice/src/data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)

# Mettre dans un commentaire le numéro de la question
# Question 1

total_params=[]
quant_col=[]
num=0

for colonne in contenu.columns:

    if contenu[colonne].dtype == 'int64' or contenu[colonne].dtype == 'float64':
        quant_col.append(colonne)
# Question 2
for col in quant_col:
    res=contenu[col]
    mean_val=res.mean() #2.1
    median_val=res.median() #2.2
    mode_val=res.mode()[0] #2.3
    std_val=res.std() #2.4
    mad_val=(res-mean_val).abs().mean() #2.5
    range_val=res.max()-res.min() #2.6
    num=num+1 
    params=pd.Series({
        "Colonne": num,
        'Moyenne': mean_val,
        'Médiane': median_val,
        'Mode': mode_val,
        'Écart-type': std_val,
        'Déviation absolue moyenne': mad_val,
        'Étendue': range_val
    })
    
    total_params.append(params.round(2))
    
res1 = pd.DataFrame(total_params).set_index('Colonne')

#Question 3
print("\n total_params:" ,res1)

# Question 4
quantiles=contenu[quant_col].quantile([0.25,0.5,0.75,0.1,0.9])
distance=pd.DataFrame({
    'Distance interquartile ': quantiles.loc[0.75] - quantiles.loc[0.25],
    'Distance interdecile': quantiles.loc[0.9] - quantiles.loc[0.1]
}).round(2)

print("\n Distance interquartile et interdecile:" ,distance)

# Question 5
for col in quant_col:
    plt.figure()
    plt.boxplot(contenu[col].dropna(), vert=True, patch_artist=True)
    plt.title(f"Boîte à moustache de la colonne: {col}")
    plt.ylabel("Valeurs")
    
    boxplot_image = os.path.join("Seance-03/Exercice/src/data", f"boxplot_{col}.png")
    plt.savefig(boxplot_image)
    plt.close()

# Question 6
with open("Seance-03/Exercice/src/data/island-index.csv","r",encoding='utf-8') as fichier:
    islands = pd.read_csv(fichier)

#Question7
surface_col = pd.to_numeric(islands['Surface (km²)'].replace(',', '', regex=True))

bounds = [0, 10, 25, 50, 100, 2500, 5000, 10000, np.inf]
labels = [
    "0 < Surface <= 10 km²",    
    "10 < Surface <= 25 km²",   
    "25 < Surface <= 50 km²",   
    "50 < Surface <= 100 km²",  
    "100 < Surface <= 2500 km²", 
    "2500 < Surface <= 5000 km²", 
    "5000 < Surface <= 10000 km²",
    "Surface > 10000 km²"       
]
categories = pd.cut(surface_col, bins=bounds, labels=labels, right=True, include_lowest=True)
categories_nombres = categories.value_counts().sort_index()
print(categories_nombres)