import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding="latin-1")

# print(df.head())
# print(df.shape)
# print(df.info())

print(df.isnull().sum())        # missing values per column
print(df.duplicated().sum())    # number of duplicate rows

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

df = df.drop_duplicates()
df.to_csv("superstore_clean.csv", index=False)
print("Cleaned file saved!")

print(df.shape)
print(df.info())
