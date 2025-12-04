import pandas as pd
json=pd.read_json("pandas/sample_Data.json")
print('Display the 5 rows of first')
print(json.head(5))
print('Display the 5 rows of last')
print(json.tail(5))