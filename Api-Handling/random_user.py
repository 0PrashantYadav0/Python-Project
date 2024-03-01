import requests
import json

def fetch_random_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    res = requests.get(url)
    data = res.json()
    if data['statusCode'] and "data" in data:
        user_data = data['data']
        user_name = user_data["login"]["username"]
        location = user_data["location"]["country"]
        return user_name, location
    else:
        raise Exception("Failed to fetch user data")



def main():
    try:
        user_name, location = fetch_random_user()
        print(f"User name: {user_name}, Location: {location}")
    finally:
        print("Exiting the program")




if __name__ == "__main__":
    main()
