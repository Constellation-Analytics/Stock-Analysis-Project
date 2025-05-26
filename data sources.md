# yfinance data sources

## Market Index:
What we need:  [Historical Data, Current price]

#### Historical Data
```python
import yfinance as yf
import pandas as pd

#Create a df with the close history for each stock om a list 
def get_stock_history(stock_list, period, spans=[30, 60, 180]):
    """
    Fetch historical closing prices and EMA for a list of stocks.

    Parameters:
        stock_list (list): List of stock tickers.
        period (str): Time period for the history (e.g. '1y', '5y').
        spans (list): EMA periods to calculate.

    Returns:
        DataFrame: Combined stock history with EMA columns.
    """

    #Create empty list
    df_index = []

    #Create loop actions for each stock in a list of stocks
    for stock in stock_list:
        tick = yf.Ticker(stock)
        df = tick.history(period=period)
        df['Stock'] = stock
        df.reset_index(inplace = True)
        df['Date'] = df['Date'].dt.date
        df = df[['Date','Stock','Close']]
        #Add EMA columns
        for span in spans:
            df[f'EMA_{span}'] = df['Close'].ewm(span=span, adjust=False).mean()
        df_index.append(df)

    #Combine the dataframes for each stock in the list
    df_all = pd.concat(df_index, ignore_index=True)

    # sort values and reset the index
    df_all = df_all.sort_values(by='Date', ascending=False)
    df_all = df_all.reset_index(drop=True)
    
    return df_all

#example 
index_list = ['^AORD', '^AXJO']
get_stock_history(index_list,"5y").head()


```

#### Current price
```python
import yfinance as yf
import pandas as pd

index_list = ['^AORD', '^AXJO']

data = []

for stock in index_list:
    tick = yf.Ticker(stock)
    price = tick.info.get("regularMarketPrice")  # safer with .get()
    data.append({"Stock": stock, "Price": price})

df_index = pd.DataFrame(data)
df_index

```

## My Portfolio:
What we need: [Current price, Historical Data, Dividends history, Last close price]
 
#### Current price
```python
import yfinance as yf

#Print the price for each stock
my_list = ['ETHI.AX', 'IEM.AX', 'IOO.AX', 'IOZ.AX','IXJ.AX','NDQ.AX','SYI.AX']

for stock in my_list:
    tick = yf.Ticker(stock)
    print(stock+":",tick.info["regularMarketPrice"])
```
#### Historical Data
```python
import yfinance as yf
import pandas as pd

#Create a df with the close history for each stock om a list 
def get_stock_history(stock_list,period):

    #Create empty list
    df_index = []

    #Create loop actions for each stock in a list of stocks
    for stock in stock_list:
        tick = yf.Ticker(stock)
        df = tick.history(period=period)
        df['Stock'] = stock
        df.reset_index(inplace = True)
        df['Date'] = df['Date'].dt.date
        df_filtered = df[['Date','Stock','Close']]
        df_index.append(df_filtered)

    #Combine the dataframes for each stock in the list
    df_all = pd.concat(df_index, ignore_index=True)

    #Add EMA columns
    df_all['EMA_30'] = df_all['Close'].ewm(span=30, adjust=False).mean()
    df_all['EMA_60'] = df_all['Close'].ewm(span=60, adjust=False).mean()
    df_all['EMA_180'] = df_all['Close'].ewm(span=180, adjust=False).mean()

    # sort values and reset the index
    df_all = df_all.sort_values(by='Date', ascending=False)
    df_all = df_all.reset_index(drop=True)
    
    return df_all

#example 
index_list = ['^AORD', '^AXJO']
get_stock_history(index_list,"5y").head()

```
#### Dividends history
```python
import yfinance as yf

#Print the dividend history for each stock
my_list = ['ETHI.AX', 'IEM.AX', 'IOO.AX', 'IOZ.AX','IXJ.AX','NDQ.AX','SYI.AX']

for stock in my_list:
    try:
        ticker = yf.Ticker(stock)
        div = ticker.dividends
        print(f"{stock}: {div}")

    except Exception as e:
        print(f"{stock}: Error - {e}")
```
