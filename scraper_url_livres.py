"""
scraper_url_livres.py

Script Python permettant de récupérer (scraper) les URL de tous les livres d'une catégorie donnée sur le site 'Books to Scrape' (https://books.toscrape.com).

Fonctionnalités principales :
- Extraction automatisée des URL des livres sur chaque page d'une catégorie précise.
- Gestion automatique de la pagination jusqu'à la dernière page disponible.
- Sauvegarde des URLs extraites dans un fichier CSV structuré.
Usage :
Exécuter directement dans un terminal :
    python scraper_url_livres.py
"""
import requests
from bs4 import BeautifulSoup
import csv

# Fonction pour récupérer les URL des livres sur une page précise
def get_books_urls(category_url, csv_filename):
    """Scrape les URLs des livres d'une catégorie et les enregistre dans un fichier CSV."""
    base_url = "https://books.toscrape.com/catalogue/"
    book_urls = []

    while category_url:
        response = requests.get(category_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extraire les URLs des livres
        for book in soup.select("h3 a"):
            book_url = base_url + book["href"].replace("../../", "")
            book_urls.append(book_url)

        # Vérifier s'il y a une page suivante
        next_page = soup.select_one("li.next a")
        if next_page:
            category_url = "/".join(category_url.split("/")
                                    [:-1]) + "/" + next_page["href"]
        else:
            category_url = None  # Fin de la pagination

    # Sauvegarde dans le CSV
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["book_url"])  # En-tête
        for url in book_urls:
            writer.writerow([url])  # Écriture des URLs

    print(f"✅ Les URLs des livres ont été enregistrées dans {csv_filename}")
    return book_urls


# Exécution du script (à supprimer si tu veux juste l'importer ailleurs)
if __name__ == "__main__":
    category_url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
    csv_filename = "output/science_books_urls.csv"
    get_books_urls(category_url, csv_filename)
