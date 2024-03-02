import requests
import json
url = "https://api.freeapi.app/api/v1/todos"

def fetch_todos():
    res = requests.get(url)
    data = res.json()
    if data['statusCode'] == 200 and "data" in data:
        todos = data['data']
        return todos, data["message"]
    else:
        return None, data["message"]

def print_todos(todos):
    for todo in todos:
        print('*'*50)
        print(f"{todo['_id']} ->\n\t{todo['title']}\n\t{todo['description']}")
        print('*'*50)

def fetch_todos_by_id(id):
    res = requests.get(f"{url}/{id}")
    data = res.json()
    if data['statusCode'] == 200 and "data" in data:
        return data['data']
    else:
        return None
