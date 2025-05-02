"""
Script de scraping pour extraire les informations de toutes les catégories de livres
sur Books to Scrape et les enregistrer dans des fichiers CSV distincts.

Ce script fonctionne de manière modulaire et repose sur l'utilisation des fonctions
suivantes :

- `get_category_urls()`: Récupère toutes les URLs des catégories du site.
- `scrape_category(category_url, output_filename)`: Scrape tous les livres d'une catégorie et sauvegarde les données dans un fichier CSV.

L'objectif est d'extraire les données de toutes les catégories disponibles sur le site,
chaque catégorie ayant son propre fichier CSV de sortie.
"""

import requests
from bs4 import BeautifulSoup
import os
from scraper_category import scrape_category
from scraper_single import scrape_book_data
from scraper_url_livres import get_books_urls

BASE_URL = "https://books.toscrape.com/"


def get_categories():
    """Récupère toutes les catégories du site avec leurs URLs, en ignorant la première (Books)."""
    response = requests.get(BASE_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    categories = {}
    
    # Sélectionner tous les liens des catégories et ignorer le premier (Books)
    category_links = soup.select(".side_categories ul li a")[1:]

    for link in category_links:
        category_name = link.text.strip()
        category_url = BASE_URL + link["href"]
        categories[category_name] = category_url

    return categories


def scrape_full_site():
    """Scrape tout le site Books to Scrape en récupérant chaque catégorie."""
    categories = get_categories()  # Récupère toutes les catégories disponibles

    for category_name, category_url in categories.items():
        print(f"📂 Scraping la catégorie : {category_name} ...")

        # Définir un nom de fichier CSV unique pour chaque catégorie
        csv_filename = f"output/{category_name.replace(' ', '_').lower()}.csv"

        # Scraper la catégorie et enregistrer les données
        scrape_category(category_url, csv_filename)

    print("Tous les livres du site ont été scrappés avec succès !")


# Lancer le scraper
if __name__ == "__main__":
    scrape_full_site()
