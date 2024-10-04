import sqlite3
import random

# SQLite Database Setup
DATABASE_FILE = 'data.db'

def init_db():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS codes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category1 TEXT,
                    category2 TEXT,
                    code TEXT
                )''')
    conn.commit()
    conn.close()

def generate_unique_code(category1, category2):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()

    # Check for existing codes for the category combination
    c.execute("SELECT code FROM codes WHERE category1 = ? AND category2 = ?", (category1, category2))
    existing_codes = [row[0] for row in c.fetchall()]

    # Generate a random code based on the categories
    code = f"{random.choice(get_items(category1))}-{random.choice(get_items(category2))}"

    # Ensure it's unique
    while code in existing_codes:
        code = f"{random.choice(get_items(category1))}-{random.choice(get_items(category2))}"

    # Save to the database
    c.execute("INSERT INTO codes (category1, category2, code) VALUES (?, ?, ?)", (category1, category2, code))
    conn.commit()
    conn.close()

    return code

def get_items(category):
    items = {
        'Animals': ['Lion', 'Tiger', 'Elephant', 'Wolf', 'Fox'],
        'Colors': ['Red', 'Blue', 'Green', 'Yellow', 'Black'],
        'Trees': ['Oak', 'Maple', 'Pine', 'Birch', 'Cedar'],
        'Flowers': ['Rose', 'Lily', 'Tulip', 'Daisy', 'Orchid']
    }
    return items.get(category, [])

# Initialize the DB when script runs
init_db()
