import csv
from pathlib import Path

CSV_FILE = Path(__file__).parent / "export_test_data" / "login.data.csv"


def get_datas():
    with open(CSV_FILE, "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_data():
    datas = get_datas()
    return datas[0]
