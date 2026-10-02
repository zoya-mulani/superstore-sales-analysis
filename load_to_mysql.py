import pandas as pd
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

password = quote_plus("YOUR_PASSWORD_HERE")
engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/superstore?charset=utf8mb4")

df = pd.read_csv("superstore_sql.csv")

with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE orders"))

df.to_sql("orders", engine, if_exists="append", index=False, chunksize=1000)

with engine.connect() as conn:
    print(conn.execute(text("SELECT COUNT(*) FROM orders")).scalar())
