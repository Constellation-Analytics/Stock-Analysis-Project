
#### Historical Data
```dax
lastclose = 
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
        ORDERBY (market_stk_close[date], DESC),
        PARTITIONBY (market_stk_close[stock])
    ),
    [previousclose]
)

```
