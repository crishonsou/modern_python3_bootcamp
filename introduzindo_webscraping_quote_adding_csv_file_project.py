import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter

base_url = "http://quotes.toscrape.com"

def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        response = requests.get(f"{base_url}{url}")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio-link": quote.find("a")["href"]
                })
        next_button = soup.find(class_="next")
        url =  next_button.find("a")["href"] if next_button else None
        sleep(1)
    return all_quotes

def write_quotes(quotes):
    with open("quotes.csv", "w", encoding="UTF-8") as csv_file:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(csv_file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


quotes = scrape_quotes()
write_quotes(quotes)
