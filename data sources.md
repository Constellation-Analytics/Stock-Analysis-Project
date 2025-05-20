# yfinance data sources

All Ordinaries Index:
- Historical Data
- Current price

Historical Data
```python
import yfinance as yf
import pandas as pd

#Create a df with the close history for each stock
index_list = ['^AORD', '^AXJO']

df_index = []

for stock in index_list:
    tick = yf.Ticker(stock)
    df = tick.history(period="1d")
    df['Stock'] = stock
    df.reset_index(inplace = True)
    df['Date'] = df['Date'].dt.date
    df_filtered = df[['Date','Stock','Close']]
    df_index.append(df_filtered)

df_all = pd.concat(df_index, ignore_index=True)
df_all
```

Current price
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

My Portfolio:
- Current price
- Dividends history
- Last close price 

```python
import yfinance as yf

#Print the price for each stock
my_list = ['ETHI.AX', 'IEM.AX', 'IOO.AX', 'IOZ.AX','IXJ.AX','NDQ.AX','SYI.AX']

for stock in my_list:
    tick = yf.Ticker(stock)
    print(stock+":",tick.info["regularMarketPrice"])
```
```python
import yfinance as yf

#Print the dividend history for each stock
my_list = ['ETHI.AX', 'IEM.AX', 'IOO.AX', 'IOZ.AX','IXJ.AX','NDQ.AX','SYI.AX']

for stock in my_list:
    try:
        tick = yf.Ticker(stock)
        div = ticker.dividends
        print(f"{stock}: {div}")

    except Exception as e:
        print(f"{stock}: Error - {e}")
```
```python
import yfinance as yf
import pandas as pd

my_list = ['ETHI.AX', 'IEM.AX', 'IOO.AX', 'IOZ.AX','IXJ.AX','NDQ.AX','SYI.AX']

df_stocks = []
for stock in my_list:
    tick = yf.Ticker(stock)
    df = tick.history(period="1d")
    df['Stock'] = stock
    df.reset_index(inplace = True)
    df_filtered = df[['Date','Stock','Close']]
    df_stocks.append(df_filtered)

df_all = pd.concat(df_stocks, ignore_index=True)
df_all
```
