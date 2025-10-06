import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

def setup_database():
    """Connects to the SQLite database and creates the customers table if it doesn't exist."""
    conn = sqlite3.connect('customer_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            contact_method TEXT
        )
    ''')
    conn.commit()
    conn.close()
