import sqlite3
import bcrypt
from datetime import datetime

DB_NAME = "smart_health.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password_hash TEXT, email TEXT, age INTEGER, gender TEXT, health_history TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS recommendations
                 (id INTEGER PRIMARY KEY, user_id INTEGER, type TEXT, content TEXT, date TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS chat_interactions
                 (id INTEGER PRIMARY KEY, user_id INTEGER, message TEXT, response TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password, email, age, gender, health_history):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        c.execute("INSERT INTO users (username, password_hash, email, age, gender, health_history) VALUES (?, ?, ?, ?, ?, ?)",
                  (username, password_hash, email, age, gender, health_history))
        conn.commit()
        return True, "Success"
    except sqlite3.IntegrityError:
        return False, "Username already exists"
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    if user and bcrypt.checkpw(password.encode(), user[1]):
        return user[0]
    return None

def get_user_profile(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT age, gender, health_history, email FROM users WHERE id = ?", (user_id,))
    profile = c.fetchone()
    conn.close()
    return {"age": profile[0], "gender": profile[1], "health_history": profile[2], "email": profile[3]}

def update_user_profile(user_id, age, gender, health_history):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET age = ?, gender = ?, health_history = ? WHERE id = ?",
              (age, gender, health_history, user_id))
    conn.commit()
    conn.close()

def save_recommendation(user_id, rec_type, content):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO recommendations (user_id, type, content, date) VALUES (?, ?, ?, ?)",
              (user_id, rec_type, content, date))
    conn.commit()
    conn.close()

def get_recommendations(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT type, content, date FROM recommendations WHERE user_id = ? ORDER BY date DESC", (user_id,))
    recs = [{"type": r[0], "content": r[1], "date": r[2]} for r in c.fetchall()]
    conn.close()
    return recs

def save_chat_interaction(user_id, message, response):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO chat_interactions (user_id, message, response, date) VALUES (?, ?, ?, ?)",
              (user_id, message, response, date))
    conn.commit()
    conn.close()

def get_chat_history(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT message, response, date FROM chat_interactions WHERE user_id = ? ORDER BY date DESC", (user_id,))
    chats = [{"message": r[0], "response": r[1], "date": r[2]} for r in c.fetchall()]
    conn.close()
    return chats