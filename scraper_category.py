"""
Script de scraping pour extraire les informations des livres depuis Books to Scrape.

Ce script utilise une approche modulaire en définissant des fonctions réutilisables 
pour extraire les données d'un livre, enregistrer les résultats en CSV et télécharger 
les images correspondantes. Chaque fonction a un rôle précis :

- `scrape_book_data(url)`: Récupère les informations d'un livre à partir de son URL.
- `save_image(image_url)`: Télécharge et enregistre l'image du livre.
- `save_to_csv(data, filename)`: Stocke les données extraites dans un fichier CSV.

L'objectif est de structurer le code en unités fonctionnelles claires pour une meilleure 
réutilisabilité et maintenabilité.
"""

import csv
import requests
from bs4 import BeautifulSoup
from scraper_single import scrape_book_data, save_to_csv


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # <-- Ajout essentiel ici

def get_books_urls(category_url):
    """Récupère toutes les URLs des livres d'une catégorie (gère la pagination)."""
    book_urls = []
    while category_url:
        response = requests.get(category_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.select("h3 a"):
            book_urls.append(urljoin(category_url, link["href"]))  # ✅ Correction ici

        next_page = soup.select_one(".next a")
        category_url = urljoin(category_url, next_page["href"]) if next_page else None  # ✅ Correction pagination ici

    return book_urls


def scrape_category(category_url, output_filename):
    """Scrape tous les livres d'une catégorie et sauvegarde dans un CSV."""
    book_urls = get_books_urls(category_url) # Récupération des URLs des livres
    # Ouverture du fichier CSV en mode écriture
    with open(output_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Scraper le premier livre pour obtenir les en-têtes du CSV
        first_book_data = scrape_book_data(book_urls[0])
        writer.writerow(first_book_data.keys())
        
        # Scraper tous les livres de la catégorie et enregistrer leurs données
        for book_url in book_urls:
            book_data = scrape_book_data(book_url)
            writer.writerow(book_data.values()) # Enregistrement dans le CSV
            print(f"✅ Livre enregistré : {book_data['title']}")# Enregistrement dans le CSV


# ---- EXÉCUTION ----
if __name__ == "__main__":
    category_url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
    output_csv = "output/science_books_data.csv"

    scrape_category(category_url, output_csv) # Enregistrement dans le CSV
    print(f"Toutes les données ont été enregistrées dans {output_csv}") # Message de confirmation
