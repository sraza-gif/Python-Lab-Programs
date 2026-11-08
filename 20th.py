
import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

print("Connecting to website...")

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )

    print("Status code:", response.status_code)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("\nNEWS HEADLINES AND LINKS\n")

    count = 0

    for link in soup.find_all("a", href=True):
        headline = link.get_text(" ", strip=True)

        if headline and len(headline) > 20:
            print("Headline:", headline)
            print("Link:", link["href"])
            print("-" * 40)
            count += 1

            if count == 10:
                break

    if count == 0:
        print("No headlines found. The website HTML may have changed.")

except requests.RequestException as e:
    print("Website connection error:", e)
