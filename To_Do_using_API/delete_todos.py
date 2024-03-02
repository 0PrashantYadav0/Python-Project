import requests
url = "https://api.freeapi.app/api/v1/todos"


def delete_todos(id):
    res = requests.delete(f"{url}/{id}")
    data = res.json()
    if "data" in data:
        return data["message"]
    else:
        return data["message"]
