import yfinance as yf
import psycopg2
import os

# Load environment variables from GitHub Secrets
NEON_DB = os.getenv("NEON_DB")

def get_stock_data(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    latest = hist.iloc[-1]
    return {
        "ticker": ticker,
        "date": latest.name.date(),
        "close": float(latest["Close"])  # Convert to native float
    }

def insert_to_db(data):
    conn = psycopg2.connect(NEON_DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_data (
            ticker TEXT,
            date DATE,
            close FLOAT
        );
    """)
    cur.execute(
        "INSERT INTO stock_data (ticker, date, close) VALUES (%s, %s, %s);",
        (data["ticker"], data["date"], data["close"])
    )
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    data = get_stock_data("AAPL")
    insert_to_db(data)
