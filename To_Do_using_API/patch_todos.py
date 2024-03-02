import requests
import json
url = "https://api.freeapi.app/api/v1/todos"

def patch_todos(id, title, description):
    res = requests.patch(f"{url}/{id}",
            data=json.dumps({"title": title ,"description": description}),
            headers={"Content-Type": "application/json"})
    data = res.json()
    if data['statusCode'] == 200 and "data" in data:
        return data['data'], data["message"]
    else:
        return None, data["message"]
