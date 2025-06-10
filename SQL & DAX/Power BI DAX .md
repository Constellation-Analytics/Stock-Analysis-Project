##### Measure - Calculate change %
```sql
market_change % = 
VAR minDateWithData =
    CALCULATE (
        MIN ( 'Previous Dates'[Date] ),
        FILTER (
            ALLSELECTED ( 'Previous Dates' ),
            NOT ISBLANK ( [market_close] )
        )
    )

VAR maxDateWithData =
    CALCULATE (
        MAX ( 'Previous Dates'[Date] ),
        FILTER (
            ALLSELECTED ( 'Previous Dates' ),
            NOT ISBLANK ( [market_close] )
        )
    )

VAR minValue =
    CALCULATE (
        [market_close],
        FILTER (
            ALL ( 'Previous Dates' ),
            'Previous Dates'[Date] = minDateWithData
        )
    )

VAR maxValue =
    CALCULATE (
        [market_close],
        FILTER (
            ALL ( 'Previous Dates' ),
            'Previous Dates'[Date] = maxDateWithData
        )
    )

RETURN
    IF (
        ISBLANK ( [market_close] ),
        BLANK(),
        DIVIDE ( maxValue - minValue, minValue )
    )

```
