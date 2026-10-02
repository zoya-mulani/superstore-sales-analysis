import pandas as pd

df = pd.read_csv("superstore_clean.csv")
df.columns = df.columns.str.lower().str.replace("-", "_").str.replace(" ", "_")
df.to_csv("superstore_sql.csv", index=False)

print(df.columns.tolist())
