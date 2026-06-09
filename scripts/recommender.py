import pandas as pd

# Load fund scorecard
fund_scorecard = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

risk = input(
    "Enter Risk Appetite (Low / Moderate / High): "
)

# Simple recommender based on Sharpe Ratio
recommendations = (
    fund_scorecard
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\nTop 3 Recommended Funds")

print(
    recommendations[
        [
            "amfi_code",
            "sharpe_ratio",
            "sortino_ratio",
            "cagr"
        ]
    ]
)