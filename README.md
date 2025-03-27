
Structure du projet

books_scraper/
images/ # Dossier où sont stockées les images des livres
output/ # Dossier où sont enregistrés les fichiers CSV
venv/ # Environnement virtuel Python
scraper_single.py # Scraper pour un seul livre
scraper_category.py # Scraper pour une catégorie complète
scraper_url_livres.py # Récupération des URLs des livres d'une catégorie
scraper_all_categories.py # Scraper pour l'ensemble du site
requirements.txt # Liste des dépendances
README.md # Documentation du projet


 Description du projet:
Ce projet Python permet d’extraire automatiquement des données (prix, titre, disponibilité, images, etc.) du site Books to Scrape. Il suit une approche claire et structurée en trois étapes :
-Extraction des pages HTML
-Transformation (analyse et nettoyage des données)
-Chargement (sauvegarde des résultats en CSV et images)
(Ce script récupère toutes les catégories du site et scrape l'ensemble des livres disponibles.)
Données extraites Pour chaque livre, les informations suivantes sont enregistrées :
URL de la page produit
Code UPC
Titre
Prix (TTC et HT)
Disponibilité
Description
Catégorie
Note
URL de l'image de couverture

Technologies utilisées:
-Python 3
-Requests (récupération HTML)
-BeautifulSoup4 (parsing HTML)
-CSV (stockage des données)
-venv (environnement virtuel)

Installation:
1. Clonez le repository :
git clone https://github.com/pierrekosc/books_scraper.git
Placez-vous dans le dossier du projet :
cd books_scraper
Créez et activez l’environnement virtuel :
python -m venv venv
# Sur macOS/Linux
source venv/bin/activate
# Sur Windows
venv\Scripts\activate

Installez les dépendances nécessaires :
pip install -r requirements.txt

Comment lancer le scraper ?
Exécutez simplement la commande suivante depuis la racine du projet :
Pour scraper un seul livre :
python scraper_single.py
Pour scraper une catégorie complète :
python scraper_category.py
Pour scraper l’ensemble du site :
python scraper_all_categories.py

Gestion des fichiers exclus
Le fichier .gitignore exclut clairement :
-Le dossier venv/ (environnement virtuel)
-Le dossier images/ (images téléchargées)
Les fichiers CSV 
Les données extraites seront enregistrées dans le dossier output/ sous forme de fichiers CSV, et les images seront sauvegardées dans le dossier images/.

