import requests
import json
url = "https://api.freeapi.app/api/v1/todos"

def post_todos(title, description):
    res = requests.post(f"{url}/",
            data=json.dumps({"title": title ,"description": description}),
            headers={"Content-Type": "application/json"})
    data = res.json()
    if data['statusCode'] == 201 and "data" in data:
        return data['data'], data["message"]
    else:
        return None, data["message"]
