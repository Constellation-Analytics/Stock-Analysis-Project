# yfinance data sources

All Ordinaries Index:
- Historical Data
- Current price

```python
import yfinance as yf

# Load the All Ordinaries Index
aord = yf.Ticker("^AORD")

# Get recent historical data
aord_df = aord.history(period="5d")  # Last 5 days

# Get the latest price
aord_current = all_ords.info["regularMarketPrice"]
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
