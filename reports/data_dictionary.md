# Data Dictionary

## nav_history
- amfi_code: Mutual fund scheme code
- date: NAV date
- nav: Net Asset Value

## transactions
- investor_id: Unique investor ID
- transaction_date: Transaction date
- amfi_code: Fund scheme code
- transaction_type: SIP / Lumpsum / Redemption
- amount_inr: Transaction amount in INR
- state: Investor state
- city: Investor city
- kyc_status: Verification status

## performance
- return_1yr_pct: 1-year return
- return_3yr_pct: 3-year CAGR
- return_5yr_pct: 5-year CAGR
- sharpe_ratio: Risk-adjusted return metric
- alpha: Excess return over benchmark