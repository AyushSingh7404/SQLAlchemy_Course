import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///maindb.db", echo=True)

df = pd.read_sql("SELECT * FROM people", con=engine)

print(df)

# new_data = pd.DataFrame({
#     "name": ["Alice", "Bob"],
#     "age": [30, 25]})

# new_data.to_sql("people", con=engine, if_exists="append", index=False)
