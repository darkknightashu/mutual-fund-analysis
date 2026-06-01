import pandas as pd
import os

folder = "data"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

for file in files:
    df = pd.read_csv(os.path.join(folder, file))

    print("=" * 50)
    print(file)
    print("Shape:", df.shape)
    print(df.dtypes)
    print(df.head())