import sqlite3
import random

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
    
def generate_unique_code(category1, category2):
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            c = conn.cursor()

            c.execute("SELECT code FROM codes WHERE category1 = ? AND category2 = ?", (category1, category2))
            existing_codes = [row[0] for row in c.fetchall()]

            items1 = get_items(category1)
            items2 = get_items(category2)

            code = f"{random.choice(items1)}-{random.choice(items2)}"

            while code in existing_codes:
                code = f"{random.choice(items1)}-{random.choice(items2)}"

            c.execute("INSERT INTO codes (category1, category2, code) VALUES (?, ?, ?)", (category1, category2, code))
            conn.commit()

        return code
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


def get_items(category):
    items = {
        'Animals': ['Lion', 'Tiger', 'Elephant', 'Wolf', 'Fox','Panda'],
        'Colors': ['Red', 'Blue', 'Green', 'Yellow', 'Black'],
        'Trees': ['Oak', 'Maple', 'Pine', 'Birch', 'Cedar'],
        'Flowers': ['Rose', 'Lily', 'Sunflower', 'Daisy', 'Orchid']
    }
    return items.get(category, [])

# Initialize the DB when script runs
init_db()
