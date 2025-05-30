# SQL Table Structure

## Market Index

### market_stk_close

| Column   | Data Type |
|----------|-----------|
| date     | date      |
| code     | varchar   |
| close    | int       |
| EMA 30   | int       |
| EMA 60   | int       |
| EMA 180  | int       |

### market_stk_price

| Column        | Data Type |
|---------------|-----------|
| stock         | varchar   |
| price         | int       |
| datetime_utc  | datetime  |

## Personal Index

### personal_stk_close

| Column   | Data Type |
|----------|-----------|
| date     | date      |
| code     | varchar   |
| close    | int       |
| EMA 30   | int       |
| EMA 60   | int       |
| EMA 180  | int       |

### personal_stk_price

| Column        | Data Type |
|---------------|-----------|
| stock         | varchar   |
| price         | int       |
| datetime_utc  | datetime  |

### personal_stk_dividend

| Column   | Data Type |
|----------|-----------|
| date     | date      |
| stock    | varchar   |
| dividend | varchar   |
