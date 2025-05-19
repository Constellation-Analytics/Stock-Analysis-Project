# yfinance data sources

Data Source 

```python
import yfinance as yf

all_ords = yf.Ticker("^AORD")
all_ords_df = all_ords.history(period='1mo')
all_ords_current = all_ords.info["regularMarketPrice"]
```
