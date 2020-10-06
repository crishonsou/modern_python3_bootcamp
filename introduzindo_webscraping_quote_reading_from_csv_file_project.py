import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictReader

base_url = "http://quotes.toscrape.com"

def read_quotes(filename):
    with open(filename, "r", encoding="UTF-8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)        


def start_game(quotes):
    quote = choice(quotes)
    remaining_guesses = 4
    print("Here´s a quote: ")
    print(quote["text"]) 
    guess = ''    

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
        if guess.lower() == quote['author'].lower():
            print("CONGRATULATIONS!! You got it right!!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            response = requests.get(f"{base_url}{quote['bio-link']}")
            soup = BeautifulSoup(response.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(f"Here is a hint: The author was born on {birth_date}, {birth_place}") 
        elif remaining_guesses == 2:
            print(f"Here is a hint: The author´s first name starts with {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here is a hint: The author´s last name starts with {last_initial}")    
        else:
            print(f"Sorry! you ran out of guesses. The answer was {quote['author']}")
        
        
    again = ''
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)?")

    if again.lower() in ('yes', 'y'):
        return start_game(quotes)
    else:
        print('Ok, Goodbye!')

quotes = read_quotes("quotes.csv")
start_game(quotes)

