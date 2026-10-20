import csv
from pathlib import Path


CSV_FILE = Path(__file__).parent / "export_test_data" / "user.csv"


def get_users():
    with open(CSV_FILE, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_user():
    users = get_users()
    return users[0]


