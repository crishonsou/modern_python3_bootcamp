import requests
import pyfiglet as pf
from random import choice


msg = "Bad Jokes!"
banner = pf.figlet_format(msg, font='slant')
print(banner)


print('We have a lot of (bad) Dad Jokes.')

user_input = input('What would you like to search for?: ')

url = "https://icanhazdadjoke.com/search"

response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params={"term": user_input}).json()

num_jokes = response["total_jokes"]
random_results = response["results"]

if num_jokes > 1:
    print(f'We find {num_jokes} jokes about {user_input}! It´s super (or not). Here is one:')
    print(choice(random_results)['joke'])
elif num_jokes == 1:
    print(f'There is one joke about {user_input}. Oh my! Here we go:')
    print(response["results"][0]["joke"])
else:
    print(f'Sorry! We couldn´t find a bad Dad Joke about {user_input}. Lucky you!')

print('TUM DUM TSSSSSSSSSSSS!')




