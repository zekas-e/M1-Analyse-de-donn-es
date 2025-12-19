#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

#C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
#Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
#Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

#Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

donnees = pd.DataFrame(ouvrirUnFichier("Seance-05/Exercice/src/data/Echantillonnage-100-Echantillons.csv"))

moyennes = donnees.mean().round(0)
print("\nMoyenne par sample opinion  :", moyennes)

freq = (moyennes/moyennes.sum()).round(2)
print("\nFréquence par sample opinion :", freq)

vraix_stat = pd.Series({'Pour':852,'Contre':911,'Sans opinion':422})

for i,j in vraix_stat.items():
    vraix_freq = {i:(j/vraix_stat.sum()).round(2)}


comp=pd.DataFrame({'Fréquence sample':freq,'Fréquence réelle':vraix_freq})
print("\n", comp)

#Théorie de l'échantillonnage (intervalles de fluctuation)
#L'échantillonnage se base sur la répétitivité.
print("Résultat sur le calcul d'un intervalle de fluctuation")
for op,p in vraix_freq.items():
    marge_erreur = 1.96 * math.sqrt((p * (1 - p)) / 100)
    lower_bound = (p - marge_erreur).round(3)
    upper_bound = (p + marge_erreur).round(3)
print(f"\nIntervalle de fluctuation pour '{op}': [{lower_bound}, {upper_bound}]")


#Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.

var1=list(donnees.iloc[0])
print(var1)
freq_var1=[n/sum(var1) for n in var1]
for i,p in enumerate(freq_var1):
    marge_erreur = 1.96 * math.sqrt((p * (1 - p)) / len(var1))
    lower_bound = round((p - marge_erreur),3)
    upper_bound = round((p + marge_erreur),3)
    print(f"\nIntervalle de confiance pour l'échantillon {i+1}: [{lower_bound}, {upper_bound}]")

print("Résultat sur le calcul d'un intervalle de confiance")

#Théorie de la décision (tests d'hypothèse)
#La décision se base sur la notion de risques alpha et bêta.
#Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Théorie de la décision")

data1 = pd.read_csv('Seance-05/Exercice/src/data/Loi-normale-Test-1.csv', header=None)[0]
data2 = pd.read_csv('Seance-05/Exercice/src/data/Loi-normale-Test-2.csv', header=None)[0]

stat1,p1 = scipy.stats.shapiro(data1)
stat2,p2 = scipy.stats.shapiro(data2)

print(f"\nTest de Shapiro-Wilk pour data1: Statistique={stat1}, p-value={p1}")
print(f"Test de Shapiro-Wilk pour data2: Statistique={stat2}, p-value={p2}")

#Si p > 0,05 : on accepte l’hypothèse que les données suivent une loi normale (gaussienne).
#Si p < 0,05 : on rejette l’hypothèse (les données suivent probablement une loi exponentielle etc.)