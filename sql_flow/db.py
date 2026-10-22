
import sqlite3
import csv

DB_NAME = "test_users.db"


import csv

users = []
with open("csv.file", "r", "utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        users.append((row["id"], row["username"], row["passowrd"]))
print(users)


def create_users():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)


    cursor.execute("""
        INSERT INTO bank_users (username, password)
        VALUES ('test_user_01', 'pass123')
    """)

    cursor.execute("""
        INSERT INTO bank_users (username, password)
        VALUES ('test_user_02', 'pass456')
    """)

    cursor.execute("""
        INSERT INTO bank_users (username, password)
        VALUES ('test_user_03', 'pass789')
    """)

    users = [
        ("standard_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce")
    ]

    users1= [
        ('1', 'user1', 'pass123'),
        ('2', 'user2', 'pass456'),
        ('3', 'user3', 'pass789')
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO users (username, password)
        VALUES (?, ?)
    """, users)

    connection.commit()
    connection.close()


def get_user():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, username, password
        FROM users
        ORDER BY id
        LIMIT 1
    """)

    user = cursor.fetchone()
    connection.close()

    return user


if __name__ == "__main__":
    create_users()
    print("Users created successfully!")
    print(get_user())
