# Analyse des Dynamiques Commerciales et Prédiction des Prix en Mauritanie

Ce projet a été réalisé dans le cadre du module "Calcul Scientifique avec Python", dispensé par le Dr. Mohamed Mahmoud El Benany, au sein de la formation doctorale de l'École Doctorale des Sciences et Technologies de la Faculté des Sciences et Techniques (FST) de l'Université de Nouakchott.


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table des Matières

- [Description](#description)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Sources de Données](#sources-de-donnees)
- [Méthodologie](#methodologie)
- [Résultats](#resultats)
- [Perspectives](#perspectives)
- [Contribution](#contribution)
- [Licence](#licence)
- [Contact](#contact)

## Description

Ce projet open-source analyse les dynamiques commerciales des poissons et crustacés en Mauritanie sur la période 2005–2020, en utilisant des données historiques de commerce. Il inclut des visualisations pour comprendre les tendances des quantités et des valeurs commerciales, ainsi que des modèles d'apprentissage automatique pour prédire les valeurs commerciales. De plus, le projet explore les prix des céréales, avec un focus sur le riz, pour analyser les distributions des prix et prédire les prix de détail en fonction de facteurs tels que l'origine (local/importé) et le type de riz (entier/brisuré). Le projet est implémenté dans un notebook Jupyter, rendant l'analyse accessible et reproductible.

## Installation

Pour exécuter ce projet, vous avez besoin de Python 3.8+ installé sur votre système. Les bibliothèques Python suivantes sont requises :

- **pandas** : Pour la manipulation et l'analyse des données.
- **numpy** : Pour les calculs numériques.
- **matplotlib** : Pour les visualisations de base.
- **seaborn** : Pour des visualisations statistiques avancées.
- **scikit-learn** : Pour le prétraitement des données et la modélisation par apprentissage automatique.
- **openpyxl** : Pour lire les fichiers Excel.

Installez ces dépendances avec la commande suivante :

```bash
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
```

Si vous utilisez un environnement Jupyter Notebook ou Google Colab, assurez-vous que Jupyter est installé. Pour Jupyter, vous pouvez l'installer via :

```bash
pip install jupyter
```

## Utilisation

Le projet est implémenté dans un notebook Jupyter nommé `mini_projet.ipynb`. Pour exécuter le projet, suivez ces étapes :

1. **Téléchargez les fichiers nécessaires** :
   - Obtenez le notebook `mini_projet.ipynb`.
   - Assurez-vous d'avoir les fichiers de données : `Africa_Quantity.csv`, `Africa_Value.csv`, et `cereale_prices.xlsx`.

2. **Préparez l'environnement** :
   - Placez les fichiers de données dans le même répertoire que le notebook ou ajustez les chemins de fichiers dans le code.
   - Ouvrez le notebook dans Jupyter Notebook ou Google Colab.

3. **Exécutez le notebook** :
   - Exécutez les cellules dans l'ordre pour :
     - Charger et nettoyer les données.
     - Générer des visualisations (graphiques en ligne, boîtes à moustaches, nuages de points).
     - Entraîner et évaluer les modèles Random Forest pour la prédiction des valeurs commerciales et des prix du riz.

4. **Sorties attendues** :
   - Visualisations des dynamiques commerciales et des distributions des prix.
   - Métriques de performance des modèles (RMSE, R²) pour les prédictions.
   - Prédictions spécifiques, comme la valeur des exportations de poisson en 2025.

**Note** : Les fichiers de données ne sont pas inclus dans ce dépôt en raison de restrictions d'accès. Veuillez contacter le mainteneur pour obtenir les fichiers ou utilisez vos propres données avec une structure similaire (voir [Sources de Données](#sources-de-donnees)).

## Sources de Données

Le projet utilise deux ensembles de données principaux :

- **Données commerciales** :
  - **Fichiers** : `Africa_Quantity.csv` et `Africa_Value.csv`.
  - **Contenu** : Données historiques sur les quantités (en tonnes) et les valeurs (en unités monétaires) des échanges commerciaux de poissons et crustacés pour divers pays africains, avec un focus sur la Mauritanie.
  - **Colonnes** : Incluent "Country", "TradeType" (Import/Export), "Product" (Fish, Crustaceans), "Year" (2005–2020), "Quantity", et "Value".
  - **Exemple** :
    | Année | Produit     | Type de Commerce | Quantité (tonnes) | Valeur (unités) |
    |-------|-------------|------------------|-------------------|-----------------|
    | 2019  | Poisson     | Import           | 4 320             | 1 284           |
    | 2020  | Poisson     | Export           | 253 061           | 203 316         |
    | 2020  | Crustacés   | Export           | 2 151             | 17 763          |

- **Données sur les prix des céréales** :
  - **Fichier** : `cereale_prices.xlsx` (feuille "Cereale").
  - **Contenu** : Informations sur les prix des céréales, avec un focus sur le riz, incluant les colonnes "Ceréale" (e.g., Riz_entier, Riz_brisure), "Origine" (Locale, Imoptée), "Prix_detail_MRO_Kg", et "Prix_gros_MRO_Kg".
  - **Exemple** :
    | Ceréale     | Origine | Prix détail (MRO/kg) | Prix gros (MRO/kg) | Rice_Type |
    |-------------|---------|----------------------|--------------------|-----------|
    | Riz_entier  | Locale  | 26                   | -                  | Entier    |
    | Riz_brisure | Importé | 500                  | 480                | Brisure   |
    | Riz_entier  | Locale  | 300                  | 280                | Entier    |

**Note** : Les données doivent être obtenues séparément, car elles ne sont pas incluses dans le dépôt. Assurez-vous que les fichiers respectent la structure décrite pour une exécution correcte.

## Méthodologie

Le projet suit une méthodologie structurée en trois étapes principales :

1. **Nettoyage des Données** :
   - Suppression des espaces dans les noms de colonnes, élimination des lignes et colonnes vides, et conversion des chaînes numériques en valeurs numériques.
   - Filtrage des données pour se concentrer sur la Mauritanie (données commerciales) et le riz (données sur les prix).
   - Gestion des valeurs aberrantes (par exemple, prix > 1000 MRO/kg considérés comme des erreurs).

2. **Visualisation** :
   - **Données commerciales** : Graphiques en ligne montrant les quantités commerciales par type (Import/Export) et produit (Poisson, Crustacés) sur 2005–2020.
   - **Prix du riz** : Graphiques à barres pour les comptes par type et origine, boîtes à moustaches pour les distributions des prix, et nuages de points pour la relation entre prix de détail et de gros.

3. **Modélisation par Apprentissage Automatique** :
   - Utilisation de modèles Random Forest (y compris une implémentation personnalisée pour les prix du riz) pour prédire les valeurs commerciales et les prix de détail.
   - Prétraitement des données avec `OneHotEncoder` pour les variables catégoriques (par exemple, Origine, Rice_Type) et `StandardScaler` pour les variables numériques (par exemple, Prix_gros_MRO_Kg).
   - Évaluation des modèles avec des métriques comme RMSE et R².

## Résultats

- **Dynamiques Commerciales** :
  - Les visualisations montrent que la Mauritanie est un exportateur net de poissons et crustacés, avec des exportations significatives (par exemple, 253 061 tonnes de poisson exportées en 2020 contre 3 770 tonnes importées).
  - Le modèle Random Forest pour la prédiction des valeurs commerciales a atteint une précision élevée avec un R² de 0,97 et une RMSE de 9 597,24. Une prédiction pour 2025 estime une valeur d’exportation de poisson de 170 958,02 unités pour 270 000 tonnes.

- **Prix du Riz** :
  - Les analyses révèlent des différences de prix selon l’origine (riz importé plus cher que le riz local) et le type (entier vs. brisé).
  - Une faible corrélation (0,081) entre les prix de détail et de gros suggère que d’autres facteurs (demande, logistique) influencent les prix.
  - Les résultats de la prédiction des prix du riz ne sont pas entièrement disponibles, mais le modèle utilise des caractéristiques comme l’origine, le type de riz, et le prix de gros.

## Perspectives

Les perspectives pour ce projet incluent :
- **Extension géographique** : Analyser les dynamiques commerciales d’autres pays africains ou d’autres produits pour une comparaison régionale.
- **Amélioration des modèles** : Intégrer des facteurs supplémentaires (inflation, saisonnalité, prix mondiaux) pour améliorer la précision des prédictions de prix.
- **Exploration des politiques** : Étudier l’impact des politiques commerciales ou des subventions sur les prix du riz et les exportations de poisson.
- **Analyse temporelle** : Prolonger la période d’analyse ou inclure des données géospatiales pour explorer les tendances à long terme et les influences régionales.

## Contribution

Les contributions sont les bienvenues ! Si vous identifiez des problèmes ou avez des suggestions d’amélioration :
1. Ouvrez un **issue** pour signaler un bug ou proposer une fonctionnalité.
2. Soumettez une **pull request** avec vos modifications, en suivant les bonnes pratiques de codage et en documentant vos changements.

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE.md](https://opensource.org/licenses/MIT) pour plus de détails.

## Contact

Pour toute question ou feedback, veuillez contacter Cheikh Abdelkader Ahmed Telmoud cheikhahmedtelmoud@gmail.com.