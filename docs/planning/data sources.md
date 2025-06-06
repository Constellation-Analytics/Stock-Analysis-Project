# yfinance data sources

## Market Index:
What we need:  [Historical Data, Current price]

#### Historical Data
```python
import yfinance as yf
import pandas as pd
from datetime import datetime

def get_stock_history(stock_list, period, spans=[30, 60, 180], watermark=None):
    """
    Fetch historical closing prices and exponential moving averages (EMAs)
    for a list of stocks using Yahoo Finance data.

    Parameters:
        stock_list (list): List of stock ticker symbols (e.g., ['^AORD', '^AXJO']).
        period (str): Time range for fetching historical data (e.g., '1y', '5y').
        spans (list): List of integer values representing EMA periods to calculate.
        watermark (str or datetime.date, optional): Only return rows with a date
            after this value. Can be a string ('YYYY-MM-DD') or a date object.

    Returns:
        pd.DataFrame: Combined stock data including Date, Stock, Close, and EMA columns.
    """

    df_index = []

    for stock in stock_list:
        tick = yf.Ticker(stock)
        df = tick.history(period=period)
        df['Stock'] = stock
        df.reset_index(inplace=True)
        df['Date'] = df['Date'].dt.date
        df = df[['Date', 'Stock', 'Close']]

        # Add EMA columns
        for span in spans:
            df[f'EMA_{span}'] = df['Close'].ewm(span=span, adjust=False).mean()

        df_index.append(df)

    # Combine all stock data
    df_all = pd.concat(df_index, ignore_index=True)

    # Filter by watermark if provided
    if watermark:
        if isinstance(watermark, str):
            watermark = datetime.strptime(watermark, '%Y-%m-%d').date()
        df_all = df_all[df_all['Date'] > watermark]

    # Sort by date (descending) and reset index
    df_all = df_all.sort_values(by='Date', ascending=False).reset_index(drop=True)
    
    return df_all

# Example usage
index_list = ['^AORD', '^AXJO']
get_stock_history(index_list, "5y")

```

#### Current price
```python
import yfinance as yf
import pandas as pd
from datetime import datetime, timezone

def get_current_price(stock_list):
    """
    Fetches the current market price for a list of stock tickers.

    Parameters:
    - stock_list (list): A list of stock ticker symbols (e.g., ['^AORD', '^AXJO']).

    Returns:
    - DataFrame: A DataFrame containing the stock symbol, current market price, and 
      the UTC datetime when the data was fetched.
    """
    data = []
    
    for stock in stock_list:
        tick = yf.Ticker(stock)
        price = tick.info.get("regularMarketPrice")
        now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        data.append({"stock": stock, "price": price, "datetime_utc": now_utc})
    
    return pd.DataFrame(data)

# Example usage
index_list = ['^AORD', '^AXJO']
get_current_price(index_list)


```

## My Portfolio:
What we need: [Historical Data, Current price, Dividends history]

#### Historical Data
```python
import yfinance as yf
import pandas as pd
from datetime import datetime

def get_stock_history(stock_list, period, spans=[30, 60, 180], watermark=None):
    """
    Fetch historical closing prices and exponential moving averages (EMAs)
    for a list of stocks using Yahoo Finance data.

    Parameters:
        stock_list (list): List of stock ticker symbols (e.g., ['^AORD', '^AXJO']).
        period (str): Time range for fetching historical data (e.g., '1y', '5y').
        spans (list): List of integer values representing EMA periods to calculate.
        watermark (str or datetime.date, optional): Only return rows with a date
            after this value. Can be a string ('YYYY-MM-DD') or a date object.

    Returns:
        pd.DataFrame: Combined stock data including Date, Stock, Close, and EMA columns.
    """

    df_index = []

    for stock in stock_list:
        tick = yf.Ticker(stock)
        df = tick.history(period=period)
        df['Stock'] = stock
        df.reset_index(inplace=True)
        df['Date'] = df['Date'].dt.date
        df = df[['Date', 'Stock', 'Close']]

        # Add EMA columns
        for span in spans:
            df[f'EMA_{span}'] = df['Close'].ewm(span=span, adjust=False).mean()

        df_index.append(df)

    # Combine all stock data
    df_all = pd.concat(df_index, ignore_index=True)

    # Filter by watermark if provided
    if watermark:
        if isinstance(watermark, str):
            watermark = datetime.strptime(watermark, '%Y-%m-%d').date()
        df_all = df_all[df_all['Date'] > watermark]

    # Sort by date (descending) and reset index
    df_all = df_all.sort_values(by='Date', ascending=False).reset_index(drop=True)
    
    return df_all

# Example usage
index_list = ['ETHI.AX', 'IEM.AX', 'IOO.AX', 'IOZ.AX','IXJ.AX','NDQ.AX','SYI.AX']
get_stock_history(index_list, "5y")

```

#### Current price
```python
import yfinance as yf
import pandas as pd
from datetime import datetime, timezone

def get_current_price(stock_list):
    """
    Fetches the current market price for a list of stock tickers.

    Parameters:
    - stock_list (list): A list of stock ticker symbols (e.g., ['^AORD', '^AXJO']).

    Returns:
    - DataFrame: A DataFrame containing the stock symbol, current market price, and 
      the UTC datetime when the data was fetched.
    """
    data = []
    
    for stock in stock_list:
        tick = yf.Ticker(stock)
        price = tick.info.get("regularMarketPrice")
        now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        data.append({"stock": stock, "price": price, "datetime_utc": now_utc})
    
    return pd.DataFrame(data)

# Example usage
index_list = ['ETHI.AX', 'IEM.AX', 'IOO.AX', 'IOZ.AX','IXJ.AX','NDQ.AX','SYI.AX']
get_current_price(index_list)


```

#### Dividends history
```python
def get_dividend_history(stock_list, watermark=None):
    """
    Fetches dividend history for a list of stocks using yfinance.

    Args:
        stock_list (list of str): List of stock tickers (e.g. ['IOZ.AX', 'NDQ.AX']).
        watermark (str or datetime.date, optional): If provided, filters dividends to only include
            those after this date. Should be in 'YYYY-MM-DD' format if string.

    Returns:
        pandas.DataFrame: A combined dataframe of dividend history with columns:
            ['Date', 'Stock', 'Dividends'], sorted by date descending.
    """

    df_index = []

    for stock in stock_list:
        tick = yf.Ticker(stock)
        div = tick.dividends
        df = div.reset_index()
        df['Date'] = df['Date'].dt.date
        df['Stock'] = stock
        df = df[['Date', 'Stock', 'Dividends']]
        df_index.append(df)

    # Combine all stock data
    df_all = pd.concat(df_index, ignore_index=True)

    # Filter by watermark if provided
    if watermark:
        if isinstance(watermark, str):
            watermark = datetime.strptime(watermark, '%Y-%m-%d').date()
        df_all = df_all[df_all['Date'] > watermark]

    # Sort by date (descending) and reset index
    df_all = df_all.sort_values(by='Date', ascending=False).reset_index(drop=True)
    
    return df_all

# Example usage
index_list = ['ETHI.AX', 'IEM.AX', 'IOO.AX', 'IOZ.AX','IXJ.AX','NDQ.AX','SYI.AX']
get_dividend_history(index_list)
```
