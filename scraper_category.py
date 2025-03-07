import csv
import requests
from bs4 import BeautifulSoup
from scraper_single import scrape_book_data, save_to_csv


def get_books_urls(category_url):
    """Récupère toutes les URLs des livres d'une catégorie (gère la pagination)."""
    book_urls = []

    while category_url:
        response = requests.get(category_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.select("h3 a"):
            book_urls.append(
                "https://books.toscrape.com/catalogue/" + link["href"].replace("../", ""))

        next_page = soup.select_one(".next a")
        category_url = "https://books.toscrape.com/catalogue/" + \
            next_page["href"] if next_page else None

    return book_urls


def scrape_category(category_url, output_filename):
    """Scrape tous les livres d'une catégorie et sauvegarde dans un CSV."""
    book_urls = get_books_urls(category_url)

    with open(output_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        first_book_data = scrape_book_data(book_urls[0])
        writer.writerow(first_book_data.keys())

        for book_url in book_urls:
            book_data = scrape_book_data(book_url)
            writer.writerow(book_data.values())
            print(f"✅ Livre enregistré : {book_data['title']}")


# ---- EXÉCUTION ----
if __name__ == "__main__":
    category_url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
    output_csv = "output/science_books_data.csv"

    scrape_category(category_url, output_csv)
    print(f"Toutes les données ont été enregistrées dans {output_csv}")
