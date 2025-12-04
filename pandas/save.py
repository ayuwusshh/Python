import pandas as pd
data={
  "Name":['Ram','Shyam','Ghanshyam'],
  "Age":[10,20,30],
  "City":['Nagpur','Mumbai','Delhi']
}

df=pd.DataFrame(data)
#print(df)

# saving in .csv
#df.to_csv("outputinCsv.csv",index=False)

# saving in .xlsx
#df.to_excel("outputinExcel.xlsx",index=False)

# saving in .json
df.to_json("OutputinJson.json",index=False)