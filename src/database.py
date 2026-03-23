import sqlite3 
from config import DB_NAME
from config import STOCKS
from fetcher import fetch_price_history
from fetcher import fetch_earnings_dates

def create_stocks_table():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS stocks (
                ticker TEXT PRIMARY KEY,
                company_name TEXT NOT NULL,
                sector TEXT NOT NULL
            )
        """)
        conn.commit()

def create_earnings_events_table():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS earnings_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker TEXT NOT NULL, 
                earnings_date DATE NOT NULL,
                actual_eps REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ticker) REFERENCES stocks(ticker)
            )
        """)
        conn.commit()

def create_price_snapshots_table():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS price_snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker TEXT NOT NULL,
                snapshot_date DATE NOT NULL,
                close_price REAL NOT NULL,
                volume INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ticker) REFERENCES stocks(ticker)
            )
        """)
        conn.commit()

def create_tables():
    create_stocks_table()
    create_earnings_events_table()
    create_price_snapshots_table()
    
def insert_stock(stock):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO stocks (ticker, company_name, sector)
            VALUES (?, ?, ?)
        """, stock)
        conn.commit()

def insert_all_stocks():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        for stock in STOCKS:
            cursor.execute("""
                INSERT INTO stocks (ticker, company_name, sector)
                VALUES (?, ?, ?)
            """, stock)
        conn.commit()
