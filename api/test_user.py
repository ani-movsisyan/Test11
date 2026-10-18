from user_client import get_user


def test_get_user():
    user = get_user("101")
    print("user id", user[id])
    print("user name", user["name"])
    print("user email", user["email"])


def test_get_user():
    data = {
        "users": [
            {"id": 101, "username": "test_user_01"},
            {"id": 102, "username": "test_user_02"},
            {"id": 103, "username": "test_user_03"}
        ]
    }

    for user1 in data["users"]:
        a = print(user1["id"], user1["username"])

    print(a)