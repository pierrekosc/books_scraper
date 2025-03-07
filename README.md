Description

Ce projet est un scraper permettant d'extraire les données de tous les livres disponibles sur le site Books to Scrape (https://books.toscrape.com/).
Il récupère les informations des livres par catégorie et enregistre les données dans des fichiers CSV.

Structure du projet

books_scraper/
│── images/ # Dossier où sont stockées les images des livres
│── output/ # Dossier où sont enregistrés les fichiers CSV
│── venv/ # Environnement virtuel Python
│── scraper_single.py # Scraper pour un seul livre
│── scraper_category.py # Scraper pour une catégorie complète
│── scraper_url_livres.py # Récupération des URLs des livres d'une catégorie
│── scraper_all_categories.py # Scraper pour l'ensemble du site
│── requirements.txt # Liste des dépendances
│── README.md # Documentation du projet
``

Prérequis

- Python 3.10+
- Bibliothèques nécessaires :
- requests
- beautifulsoup4
- csv
  os

Installation

1. Cloner le projet :

   git clone https://github.com/ton-repo/books_scraper.git
   cd books_scraper

2. Créer un environnement virtuel et l'activer :

   python -m venv venv

   source venv/bin/activate # Sur macOS/Linux

   venv\Scripts\activate # Sur Windows

3. Installer les dépendances :

   pip install -r requirements.txt

Utilisation

Scraper un seul livre

python scraper_single.py

(Ce script récupère les informations d’un seul livre à partir de son URL et enregistre les données dans un fichier CSV.)

Scraper une seule catégorie

python scraper_category.py

(Ce script récupère tous les livres d'une seule catégorie et stocke les informations dans un fichier CSV.)

Scraper tout le site

python scraper_all_categories.py

(Ce script récupère toutes les catégories du site et scrape l'ensemble des livres disponibles.)

Données extraites
Pour chaque livre, les informations suivantes sont enregistrées :

- URL de la page produit
- Code UPC
- Titre
- Prix (TTC et HT)
- Disponibilité
- Description
- Catégorie
- Note
- URL de l'image de couverture
