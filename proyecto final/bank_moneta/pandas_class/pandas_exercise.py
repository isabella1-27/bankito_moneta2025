import pandas as pd 

d = {'col1': [1,2], 'col2': [3,4]}
df = pd.DataFrame(d)

df_csv = pd.read_csv("user.csv")
print(df_csv)
print(df_csv.columns)
print(df_csv.shape)
print(df_csv.dtypes)