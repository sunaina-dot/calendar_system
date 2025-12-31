from flask_login import UserMixin
from models.db import get_db_connection

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username


def create_user(fullname, username, email, password):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO users (fullname, username, email, password) VALUES (?,?,?,?)",
        (fullname, username, email, password)
    )
    conn.commit()
    conn.close()


def get_user_by_username(username):
    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    ).fetchone()
    conn.close()
    return user


def get_user_by_id(user_id):
    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE id=?",
        (user_id,)
    ).fetchone()
    conn.close()
    if user:
        return User(user["id"], user["username"])
    return None
