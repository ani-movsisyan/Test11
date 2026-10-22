import sqlite3
import csv

db_name = "Db_name"

users = []

with open("csv.file", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        users.append(row["id"], row["username"], row["password"])
print(users)

def create_db_get_users():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("""Create Tabe if npot exist users id ineger primary key autoincremen, username Text not null, password text not null""")


    cursor.executemany("""insert into users(id, username, password), Values(?, ?, ?)""", users)

    connection.commit()
    connection.close()


def get_user():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    cursor.execute("""select id, password, username from users order by id limit 1""")

    user = cursor.fetchone()
    return user