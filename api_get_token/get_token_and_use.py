
import requests

BASE_URL = "https://test-bank.example.com/api"

def test_get_balance_with_token():

    # 1. Login
    login_response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "username": "test_user",
            "password": "test_password"
        }
    )

    assert login_response.status_code == 200

    # 2. Get token
    token = login_response.json()["access_token"]

    # 3. Use token to get account balance
    headers = {
        "Authorization": f"Bearer {token}"
    }

    balance_response = requests.get(
        f"{BASE_URL}/accounts/ACC001/balance",
        headers=headers
    )

    # 4. Check the result
    assert balance_response.status_code == 200

    balance_data = balance_response.json()

    assert "balance" in balance_data

    print("Account balance:", balance_data["balance"])









