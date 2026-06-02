-- Top 5 funds by 1-year return
SELECT
    scheme_name,
    fund_house,
    return_1yr_pct
FROM performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Transaction amount by type
SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM transactions
GROUP BY transaction_type;

-- Top 10 states by transactions
SELECT
    state,
    COUNT(*) AS transactions
FROM transactions
GROUP BY state
ORDER BY transactions DESC
LIMIT 10;