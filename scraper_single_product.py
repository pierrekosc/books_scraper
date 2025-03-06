import requests
from bs4 import BeautifulSoup
import csv
import os

# URL of the page we want to scrape
url = 'https://books.toscrape.com/catalogue/tipping-point-for-planet-earth-how-close-are-we-to-the-edge_643/index.html'

# Send a GET request to the server
response = requests.get(url)
response.raise_for_status()  # 200 -> ok 404 -> not found

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# extract information
product_page_url = url
title = soup.find('h1').text.strip()

# extract another information
table_data = soup.find_all('td')
upc = table_data[0].text.strip()
price_including_tax = table_data[3].text.strip()
price_excluding_tax = table_data[2].text.strip()
number_available = table_data[5].text.strip()

# extract descritpion product
# Trouver la section "Product Description"
description_header = soup.find("div", id="product_description")

# Si la description existe, récupérer le paragraphe suivant
if description_header:
    product_description = description_header.find_next_sibling(
        "p").text.strip()
else:
    product_description = "No description available."

# Catégorie du livre
category = soup.find("ul", class_="breadcrumb").find_all("li")[2].text.strip()

# Note du livre (étoiles)
rating_elem = soup.find("p", class_="star-rating")
review_rating = rating_elem["class"][1] if rating_elem else "No rating"

# URL de l'image
image_elem = soup.find("img")
image_url = "https://books.toscrape.com/" + \
    image_elem["src"].replace("../", "") if image_elem else "No image"
# Télécharger et enregistrer l'image
image_filename = os.path.join("images", image_url.split("/")[-1])
response = requests.get(image_url, stream=True)
if response.status_code == 200:
    with open(image_filename, "wb") as img_file:
        for chunk in response.iter_content(1024):
            img_file.write(chunk)
    print(f"Image enregistrée dans {image_filename}")
else:
    print("Erreur lors du téléchargement de l'image")

# Enregistrer les données dans un fichier CSV
csv_filename = "output/single_product.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # En-tête des colonnes
    writer.writerow(["product_page_url", "universal_product_code", "title", "price_including_tax",
                    "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"])
    # Ligne des données
    writer.writerow([product_page_url, upc, title, price_including_tax, price_excluding_tax,
                    number_available, product_description, category, review_rating, image_url])

print(f"Données enregistrées dans {csv_filename}")
