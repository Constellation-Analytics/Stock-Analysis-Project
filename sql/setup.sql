
-- stk_personal
CREATE TABLE IF NOT EXISTS stk_personal(date date, code varchar, close int, ema30 int, ema60 int, ema180 int, date_entered date);
ALTER TABLE "public"."stk_personal"
ADD CONSTRAINT "pk_stk_personal" PRIMARY KEY ("date", "code")
  
-- stk_market
CREATE TABLE IF NOT EXISTS stk_market(date date, code varchar, close int, ema30 int, ema60 int, ema180 int, date_entered date);
ALTER TABLE "public"."stk_market"
ADD CONSTRAINT "pk_stk_market" PRIMARY KEY ("date", "code")
