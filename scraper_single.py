import requests
from bs4 import BeautifulSoup
import csv
import os


def scrape_book_data(url):
    """Scrape les informations d'un livre à partir de son URL."""
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Récupération des informations du livre
    product_page_url = url
    title = soup.find('h1').text.strip()

    # Informations présentes sous forme de tableau
    table_data = soup.find_all('td')
    upc = table_data[0].text.strip()
    price_including_tax = table_data[3].text.strip()
    price_excluding_tax = table_data[2].text.strip()
    number_available = table_data[5].text.strip()

    # Récupération de la description
    description_header = soup.find("div", id="product_description")
    product_description = description_header.find_next_sibling(
        "p").text.strip() if description_header else "No description available."

    # Catégorie du livre
    category = soup.find("ul", class_="breadcrumb").find_all("li")[
        2].text.strip()

    # Évaluation du livre
    rating_elem = soup.find("p", class_="star-rating")
    review_rating = rating_elem["class"][1] if rating_elem else "No rating"

    # URL de l'image
    image_elem = soup.find("img")
    image_url = "https://books.toscrape.com/" + \
        image_elem["src"].replace("../", "") if image_elem else "No image"

    # Télécharger et sauvegarder l'image
    save_image(image_url)

    # Retourner les données sous forme de dictionnaire
    return {
        "product_page_url": product_page_url,
        "universal_product_code": upc,
        "title": title,
        "price_including_tax": price_including_tax,
        "price_excluding_tax": price_excluding_tax,
        "number_available": number_available,
        "product_description": product_description,
        "category": category,
        "review_rating": review_rating,
        "image_url": image_url
    }
# Fonction pour télécharger et enregistrer l'image


def save_image(image_url):
    # Télécharger et enregistrer l'image
    image_filename = os.path.join("images", image_url.split(
        "/")[-1])  # Chemin dans le dossier images

    response = requests.get(image_url)  # Récupère l'image
    if response.status_code == 200:
        with open(image_filename, "wb") as img_file:
            # Écrit l'image directement dans le fichier
            img_file.write(response.content)
        print(f"Image enregistrée dans {image_filename}")
    else:
        print("Erreur lors du téléchargement de l'image")
# Fonction pour enregistrer les données dans un fichier CSV


def save_to_csv(data, filename="output/single_product.csv"):
    """Sauvegarde les données d'un livre dans un fichier CSV."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Écrire l'en-tête si le fichier est vide
        if file.tell() == 0:
            writer.writerow(data.keys())
        writer.writerow(data.values())

    print(f"Données enregistrées dans {filename}")


# ---- EXÉCUTION ----
if __name__ == "__main__":
    book_url = 'https://books.toscrape.com/catalogue/tipping-point-for-planet-earth-how-close-are-we-to-the-edge_643/index.html'
    bookdata = scrape_book_data(book_url)
    save_to_csv(book_data)
