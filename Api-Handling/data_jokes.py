import requests
import json

def get_jokes():
    url = "https://official-joke-api.appspot.com/jokes/programming/random"
    response = requests.get(url)
    return response.json()

def print_joke():
    res = get_jokes()
    for index, joke in enumerate(res, start=1):
       print(f"\t{joke['setup']} \n\t{joke['punchline']}\n ")
print_joke()
