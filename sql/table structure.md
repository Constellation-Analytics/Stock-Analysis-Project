# SQL Table Structure

## Market Index

### `market_stk_close`

| Column  | Data Type | Key         |
|---------|-----------|-------------|
| date    | date      | Primary Key |
| code    | varchar   | Primary Key |
| close   | int       |             |
| EMA 30  | int       |             |
| EMA 60  | int       |             |
| EMA 180 | int       |             |

### `market_stk_price`

| Column       | Data Type | Key         |
|--------------|-----------|-------------|
| stock        | varchar   | Primary Key |
| price        | int       |             |
| datetime_utc | datetime  |             |

---

## Personal Index

### `personal_stk_close`

| Column  | Data Type | Key         |
|---------|-----------|-------------|
| date    | date      | Primary Key |
| code    | varchar   | Primary Key |
| close   | int       |             |
| EMA 30  | int       |             |
| EMA 60  | int       |             |
| EMA 180 | int       |             |

### `personal_stk_price`

| Column       | Data Type | Key         |
|--------------|-----------|-------------|
| stock        | varchar   | Primary Key |
| price        | int       |             |
| datetime_utc | datetime  |             |

### `personal_stk_dividend`

| Column   | Data Type | Key         |
|----------|-----------|-------------|
| date     | date      |             |
| stock    | varchar   | Primary Key |
| dividend | varchar   |             |
