import requests
from config import API_BASE_URL, API_TOKEN


def get_user(user_id):
    url = f"{API_BASE_URL}/users/{user_id}"
   # url1 = f"{token}/users"

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    data = response

    return data


