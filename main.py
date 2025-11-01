import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")

soup = BeautifulSoup(response.text, "html.parser")

frases = soup.find_all("span", class_="text")

for frase in frases:
    print(frase.text)