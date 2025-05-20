
-- stk_personal
CREATE TABLE IF NOT EXISTS stk_personal(date date, code varchar, close int, ema30 int, ema60 int, ema180 int, date_entered date);

-- stk_market
CREATE TABLE IF NOT EXISTS stk_market(date date, code varchar, close int, ema30 int, ema60 int, ema180 int, date_entered date);

