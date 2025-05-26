# 📈 Stock Portfolio & Market Monitor

This is a full end-to-end **cloud-based** data pipeline project that tracks the performance of my personal stock portfolio and trends in the Australian stock market. It fetches live data, stores it in the cloud, analyses trends (like moving averages and dividends), and enables visual exploration in Power BI.

---

## 🧠 Project Goals

### 🔒 My Share Portfolio
- Track how my personal stocks are performing over time
- Calculate performance based on:
  - Growth over time
  - Comparison against market indices (ASX200, All Ordinaries)
  - Comparison against inflation (CPI)
  - Dividends paid — value, frequency, and averages
  - Forecast next dividend dates
  - Trigger alerts for:
    - Large variances from moving averages
    - Upcoming dividend payouts
    - Recently paid dividends

### 📊 The Wider Market
- Monitor Australian stock indices (e.g. `^AXJO`, `^AORD`)
- Calculate Exponential Moving Averages (EMA) for trend detection
- Trigger alerts for:
  - Large variances from moving averages

---

## 🛠️ Tech Stack

| Tool           | Purpose                          |
|----------------|----------------------------------|
| `yfinance`     | Fetches historical stock data via Yahoo Finance API |
| `pandas`       | Cleans and transforms financial data |
| `Neon`         | Cloud-based PostgreSQL database for storing stock data |
| `GitHub Actions` | Automates scheduled data refresh jobs |
| `Power BI`     | Creates interactive dashboards to visualize portfolio and market trends |

---

## 🔄 Workflow

1. **Data Ingestion**
   - A scheduled Python script (via GitHub Actions) pulls daily stock data using `yfinance`
   - Includes personal stocks, ASX 200 (`^AXJO`), and All Ords (`^AORD`)
   - Calculates EMA 

2. **Data Storage**
   - Cleaned data is written to a PostgreSQL database hosted on [Neon](https://neon.tech)
   - A watermark strategy ensures only new data is inserted (no duplicates)

3. **Data Analysis**
   - EMA logic highlights moving average trends
   - Dividend tracking answers questions like:
     - When are dividends paid?
     - What’s the average payout?
     - What’s the dividend frequency?

4. **Data Visualization**
   - Power BI dashboards surface insights like:
     - Personal stock performance vs. market indices
     - Dividend history

---

## 🔜 Next Steps

- Add CPI data from an Australian source (e.g. ABS or RBA APIs)
- Build alerting system (email or Power Automate)
- Explore ETF tracking and diversification metrics

---

## 📬 Contact

Built by Paul  
For questions or ideas, feel free to open an issue or reach out.
