import yfinance as yf
import pandas as pd
import psycopg2
import os
from datetime import datetime

# Load environment variables from GitHub Secrets
NEON_DB = os.getenv("NEON_DB")

def insert_to_db(data, table):
    """
    THIS FUNCTION NEEDS TO BE UPDATED
    """
    conn = psycopg2.connect(NEON_DB)
    cur = conn.cursor()
    """)
    cur.execute(
        f"INSERT INTO {table} (ticker, date, close) VALUES (%s, %s, %s);",
        (data["ticker"], data["date"], data["close"])
    )
    conn.commit()
    cur.close()
    conn.close()
