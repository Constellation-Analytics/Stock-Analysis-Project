import pandas as pd
import os
from sqlalchemy import create_engine
from datetime import datetime

# Load environment variables from GitHub Secrets
NEON_DB = os.getenv("NEON_DB")

# Create the engine once
engine = create_engine(NEON_DB)

def insert_to_db(data: pd.DataFrame, table: str, engine):
    """
    Inserts stock data into the specified PostgreSQL table.

    Parameters:
    - data (pd.DataFrame): DataFrame with columns: 'Date', 'Stock', 'Close', 'EMA_30', 'EMA_60', 'EMA_180'.
    - table (str): Name of the target table.
    - engine: SQLAlchemy engine object.

    The function adds a 'date_entered' timestamp before inserting.
    """
    data = data.copy()
    data['date_entered'] = datetime.now()
    data.columns = ['date', 'stock', 'close', 'ema30', 'ema60', 'ema180', 'date_entered']

    with engine.connect() as connection:
        data.to_sql(table, connection, if_exists="append", index=False)
