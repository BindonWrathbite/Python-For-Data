import pyjokes
import os

# joke = pyjokes.get_jokes()
# print(joke)

files = os.listdir('.')
print(files)

import requests
url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
response_json = requests.get(url)
print_me = response_json.json()
print(print_me)