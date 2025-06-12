import os
import logging
from datetime import datetime, timezone

import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine, text

# Load environment variables from GitHub Secrets
NEON_DB = os.getenv("NEON_DB")

# Create the engine
engine = create_engine(NEON_DB)

# Set up logging 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# ----------------------------------------------------------------------------------------------------
#                                       Defining functions
# ----------------------------------------------------------------------------------------------------

def insert_to_db(data: pd.DataFrame, table: str, engine, truncate: bool = False):
    """
    Inserts data into the specified PostgreSQL table.
    
    Args:
        data (pd.DataFrame): DataFrame to insert.
        table (str): Name of the target table.
        engine: SQLAlchemy engine object.
        truncate (bool, optional): If True, truncates the table before inserting new data. Defaults to False.
    """
    if truncate:
        logger.info(f"Truncating: {table}")
        with engine.begin() as conn:
            conn.execute(text(f'TRUNCATE TABLE {table}'))

    with engine.connect() as connection:
        data.to_sql(table, connection, if_exists="append", index=False)

    logger.info(f"Inserting: {len(data)} rows, into {table}")

def get_max_date(column: str, table: str):
    """
    Gets the maximum date from the specified PostgreSQL column and table

    Args:
        column (str): Name of the target column.
        table (str): Name of the target table.
        
    Returns:
        datetime.date object for the specified PostgreSQL column and table
    """
    with engine.connect() as conn:
        result = conn.execute(text(f'SELECT MAX({column}) FROM {table}'))
        max_date = result.fetchone()[0] 
        
    return max_date

def get_stock_history(stock_list, period, spans=[30, 60, 180], watermark=None):
    """
    Fetch historical closing prices and exponential moving averages (EMAs)
    for a list of stocks using Yahoo Finance data.
    
    Args:
        stock_list (list): List of stock ticker symbols (e.g., ['^AORD', '^AXJO']).
        period (str): Time range for fetching historical data (e.g., '1y', '5y').
        spans (list, optional): List of integer values representing EMA periods to calculate. Defaults to [30, 60, 180].
        watermark (str or datetime.date, optional): Only return rows with a date after this value. Can be a string ('YYYY-MM-DD') or a date object.
    
    Returns:
        pd.DataFrame: Combined stock data including date, stock, close, and EMA columns.
    """

    df_index = []

    for stock in stock_list:
        tick = yf.Ticker(stock)
        df = tick.history(period=period)
        
        df['Stock'] = stock
        df.reset_index(inplace=True)
        df['Date'] = df['Date'].dt.date
        df['date_entered'] = datetime.now(timezone.utc)

        df = df[['Date', 'Stock', 'Close','date_entered']]
        df.columns = ['date', 'stock', 'close','date_entered']

        # Add EMA columns
        for span in spans:
            df[f'ema_{span}'] = df['close'].ewm(span=span, adjust=False).mean()

        df_index.append(df)

    # Combine all stock data
    df_all = pd.concat(df_index, ignore_index=True)

    # Filter by watermark if provided
    if watermark:
        if isinstance(watermark, str):
            watermark = datetime.strptime(watermark, '%Y-%m-%d').date()
        df_all = df_all[df_all['date'] > watermark]

    # Sort by date (descending) and reset index
    df_all = df_all.sort_values(by='date', ascending=False).reset_index(drop=True)
    
    return df_all

def get_current_price(stock_list):
    """
    Fetches the current market price for a list of stock tickers.
    
    Args:
        stock_list (list): A list of stock ticker symbols (e.g., ['^AORD', '^AXJO']).
    
    Returns:
        pd.DataFrame: A DataFrame containing the stock symbol, current market price, and the UTC datetime when the data was fetched.
    """
    data = []
    
    for stock in stock_list:
        tick = yf.Ticker(stock)
        price = tick.fast_info["last_price"]
        now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        data.append({"stock": stock, "price": price, "datetime_utc": now_utc})
    
    return pd.DataFrame(data)

def get_dividend_history(stock_list, watermark=None):
    """
    Fetches dividend history for a list of stocks using yfinance.
    
    Args:
        stock_list (list of str): List of stock tickers (e.g., ['IOZ.AX', 'NDQ.AX']).
        watermark (str or datetime.date, optional): If provided, filters dividends to only include those after this date. Should be in 'YYYY-MM-DD' format if string.
    
    Returns:
        pd.DataFrame: A combined DataFrame of dividend history with columns: ['date', 'stock', 'dividend'], sorted by date descending.
    """

    df_index = []

    for stock in stock_list:
        tick = yf.Ticker(stock)
        div = tick.dividends
        df = div.reset_index()
        df['Date'] = df['Date'].dt.date
        df['Stock'] = stock
        df = df[['Date', 'Stock', 'Dividends']]
        df.columns = ['date', 'stock', 'dividend']
        df_index.append(df)

    # Combine all stock data
    df_all = pd.concat(df_index, ignore_index=True)

    # Filter by watermark if provided
    if watermark:
        if isinstance(watermark, str):
            watermark = datetime.strptime(watermark, '%Y-%m-%d').date()
        df_all = df_all[df_all['date'] > watermark]

    # Sort by date (descending) and reset index
    df_all = df_all.sort_values(by='date', ascending=False).reset_index(drop=True)
    
    return df_all

# ----------------------------------------------------------------------------------------------------
#                                     Retrieving the data with logging
# ----------------------------------------------------------------------------------------------------

# Market Info
index_list = ['^AORD', '^AXJO']

logger.info("Fetching current prices for market indices")
market_current_price = get_current_price(index_list)
logger.info(market_current_price)

market_watermark = get_max_date('date', 'market_stk_close')
logger.info(f"Market watermark: {market_watermark}")

logger.info("Fetching market history")
market_indexs = get_stock_history(index_list, "6y", watermark=market_watermark)
logger.info(f"Market index history rows: {len(market_indexs)}")
logger.info(f"Market index history: {market_indexs}")

# My Stocks
etf_list = ['ETHI.AX', 'IEM.AX', 'IOO.AX', 'IOZ.AX','IXJ.AX','NDQ.AX','SYI.AX']

logger.info("Fetching current prices for market indices")
etf_current_price = get_current_price(etf_list)
logger.info(etf_current_price)

personal_watermark = get_max_date('date', 'personal_stk_close')
logger.info(f"Personal watermark: {personal_watermark}")

logger.info("Fetching personal stock history")
my_stocks = get_stock_history(etf_list, "6y", watermark=personal_watermark)
logger.info(f"Personal stock history rows: {len(my_stocks)}")
logger.info(f"Personal stock history: {my_stocks}")

dividend_watermark = get_max_date('date', 'personal_stk_dividend')
logger.info(f"Dividend watermark: {dividend_watermark}")

dividends = get_dividend_history(etf_list, watermark=dividend_watermark)
logger.info(f"Dividend history rows: {len(dividends)}")
logger.info(f"Dividend history: {dividends}")

# ----------------------------------------------------------------------------------------------------
#                        Inserting into the database - optimised for testing only
# ----------------------------------------------------------------------------------------------------

#insert_to_db(data: pd.DataFrame, table: str, engine, truncate: bool = False):
logger.info("Inserting data into the database (If applicable)")
insert_to_db(market_indexs,'market_stk_close',engine)
insert_to_db(my_stocks,'personal_stk_close',engine)
insert_to_db(dividends,'personal_stk_dividend',engine)
insert_to_db(market_current_price,'market_stk_price',engine,True)
insert_to_db(etf_current_price,'personal_stk_price',engine,True)
logger.info("Script complete")
