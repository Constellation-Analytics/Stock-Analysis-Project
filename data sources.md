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

```python
my_list = ['ETHI', 'IEM', 'IOO', 'IOZ','IXJ','NDQ','SYI']

for stock in my_list:
    tick = yf.Ticker(stock+".AX")
    print(stock+":",tick.info["regularMarketPrice"])
```
