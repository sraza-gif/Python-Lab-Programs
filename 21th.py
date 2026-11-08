
import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

response = requests.get(url, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Product Link"])

    for product in soup.select("article.product_pod"):
        name = product.h3.a["title"]
        price = product.select_one(".price_color").get_text(strip=True)
        link = urljoin(url, product.h3.a["href"])

        writer.writerow([name, price, link])

print("Product information saved to products.csv")
