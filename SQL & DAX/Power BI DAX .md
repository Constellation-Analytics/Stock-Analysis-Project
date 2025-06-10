
##### Calculate column - previous close (same logic applied to market and personal)
```sql
previous_close = 
VAR vRelation = SUMMARIZECOLUMNS ( 
                    market_stk_close[stock], 
                    market_stk_close[date], 
                    "previousclose", SUM(market_stk_close[close]) 
                  )
RETURN
SELECTCOLUMNS (
    OFFSET (
        -1,
        vRelation,
        ORDERBY (market_stk_close[date], ASC),
        PARTITIONBY (market_stk_close[stock])
    ),
    [previousclose]
)
```

##### Measure - Calculate change %
```sql
mkt_change % = DIVIDE(
    SUM(market_stk_close[stock])-SUM(market_stk_close[previous_close]),
    SUM(market_stk_close[stock]))
```
