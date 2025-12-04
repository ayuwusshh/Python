import pandas as pd
"""
2 types of encoding methods-->1. UTF-8, 2. Latin1
"""
# read data form the csv file
csv=pd.read_csv("pandas\sales_data_sample.csv",encoding="latin8")
#print(csv)

# read data form the excel file
xl=pd.read_excel("pandas\Product-Sales-Region.xlsx")
#print(xl)

# read data form the json file
json=pd.read_json("pandas\sample_Data.json")
#print(json)