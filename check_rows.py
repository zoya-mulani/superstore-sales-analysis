import pandas as pd

df = pd.read_csv("superstore_sql.csv")
print(df[df["row_id"].isin([6212, 6283, 6284, 6289, 6301, 6320])].T)
