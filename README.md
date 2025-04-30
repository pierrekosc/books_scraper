# BOOKS SCRAPER

## DESCRIPTION DU PROJET

Ce projet Python automatise l’extraction de données sur le site [Books to Scrape](https://books.toscrape.com), incluant : titre, prix TTC/HT, stock disponible, description, catégorie, note et image de chaque livre.

Il suit une architecture **ETL** :
- **Extraction** des pages HTML du site,
- **Transformation** des données récupérées (nettoyage et structuration),
- **Chargement** dans des fichiers CSV + téléchargement des images.

## STRUCTURE DU PROJET

```
books_scraper/
├── images/                  # Dossier de sauvegarde des images téléchargées
├── output/                  # Fichiers CSV générés
├── venv/                    # Environnement virtuel Python
├── scraper_single.py        # Scraper un seul livre
├── scraper_category.py      # Scraper une catégorie entière
├── scraper_url_livres.py    # Récupère les URLs des livres d'une catégorie
├── scraper_all_categories.py# Scraper tout le site
├── requirements.txt         # Dépendances Python
└── README.md                # Documentation du projet
```

## DONNÉES EXTRACTIBLES

Pour chaque livre, le scraper enregistre les éléments suivants :
- URL de la page produit
- Code UPC
- Titre
- Prix (TTC et HT)
- Disponibilité
- Description
- Catégorie
- Note (étoiles)
- URL de l'image de couverture

## TECHNOLOGIES UTILISÉES

- Python 3
- `requests` – Requêtes HTTP
- `beautifulsoup4` – Parsing HTML
- `csv` – Sauvegarde des données
- `venv` – Environnement virtuel Python

## INSTALLATION

1. **Cloner le projet :**
```bash
git clone https://github.com/pierrekosc/books_scraper.git
cd books_scraper
```

2. **Créer et activer l’environnement virtuel :**
```bash
python -m venv venv
# Sur macOS / Linux :
source venv/bin/activate
# Sur Windows :
venv\Scripts\activate
```

3. **Installer les dépendances :**
```bash
pip install -r requirements.txt
```

## UTILISATION

Depuis la racine du projet :

- Scraper un **livre** :
```bash
python scraper_single.py
```

- Scraper une **catégorie** :
```bash
python scraper_category.py
```

- Scraper **tout le site** :
```bash
python scraper_all_categories.py
```

## GESTION DES FICHIERS EXCLUS

Le fichier `.gitignore` exclut :
- Le dossier `venv/`
- Le dossier `images/`
- Les fichiers CSV du dossier `output/`

Les résultats sont enregistrés dans :
- `output/` pour les fichiers CSV
- `images/` pour les visuels téléchargés