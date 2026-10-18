import sqlite3

DB_NAME = "test_users.db"


def create_database():
    """Create the users table if it does not exist."""
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)

    print("Database and users table are ready.")


def add_users():
    """Insert sample test users into the database."""
    users = [
        (101, "test_user_01", "active"),
        (102, "test_user_02", "active"),
        (103, "test_user_03", "blocked")
    ]

    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()

        cursor.executemany("""
            INSERT OR IGNORE INTO users (id, username, status)
            VALUES (?, ?, ?)
        """, users)

    print("Test users added.")


def get_user(user_id):
    """Get one user by ID."""
    with sqlite3.connect(DB_NAME) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, username, status
            FROM users
            WHERE id = ?
        """, (user_id,))

        user = cursor.fetchone()

        if user is None:
            return None

        return dict(user)


def get_all_users():
    """Get all users from the database."""
    with sqlite3.connect(DB_NAME) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, username, status
            FROM users
            ORDER BY id
        """)

        return [dict(user) for user in cursor.fetchall()]


if __name__ == "__main__":
    create_database()
    add_users()

    print("\nOne user:")
    print(get_user(102))

    print("\nAll users:")
    for user in get_all_users():
        print(user)
