CREATE TABLE IF NOT EXISTS market_stk_close (
    date DATE,
    code VARCHAR(50),
    close INTEGER,
    ema_30 INTEGER,
    ema_60 INTEGER,
    ema_180 INTEGER,
    CONSTRAINT pk_market_stk_close PRIMARY KEY (date, code)
);

CREATE TABLE IF NOT EXISTS market_stk_price (
    stock VARCHAR(50),
    price INTEGER,
    datetime_utc TIMESTAMP,
    CONSTRAINT pk_market_stk_price PRIMARY KEY (stock)
);

CREATE TABLE IF NOT EXISTS personal_stk_close (
    date DATE,
    code VARCHAR(50),
    close INTEGER,
    ema_30 INTEGER,
    ema_60 INTEGER,
    ema_180 INTEGER,
    CONSTRAINT pk_personal_stk_close PRIMARY KEY (date, code)
);

CREATE TABLE IF NOT EXISTS personal_stk_price (
    stock VARCHAR(50),
    price INTEGER,
    datetime_utc TIMESTAMP,
    CONSTRAINT pk_personal_stk_price PRIMARY KEY (stock)
);

CREATE TABLE IF NOT EXISTS personal_stk_dividend (
    date DATE,
    stock VARCHAR(50),
    dividend VARCHAR(50),
    CONSTRAINT pk_personal_stk_dividend PRIMARY KEY (stock)
);
