import sqlite3
import os

def init_db():
    # Use absolute path for the database
    db_path = '/app/data/todos.db'
    db_dir = os.path.dirname(db_path)
    
    # Ensure data directory exists
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # Connect to SQLite database (this will create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create tasks table
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully!")
