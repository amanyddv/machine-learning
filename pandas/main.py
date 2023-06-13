import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
  
# }

# print(mydataset)
# myvar = pd.DataFrame(mydataset)

# print(myvar)

# a = [1, 7, 2]

# myvar = pd.Series(a)

# print(myvar)
# print(myvar[0])

# myvar = pd.Series(a, index = ["x", "y", "z"])
# print(myvar)
pd.options.display.max_rows = 9999
df = pd.read_csv('pandas/ds_salaries.csv')
# df = pd.read_json('pandas/data.json')
# print(df.to_string())
print(pd.options.display.max_rows)
# print(df.head(10))

# print(df.tail(10))

# print(df) 

# # print(df.info()) 
# print(df.head())
# df.dropna(inplace = True)

# new_df = df.dropna()
# print(new_df.info())
df.fillna(130, inplace = True)
print(df.head(10)) 

