# pip3 install virtualenv
# virtualenv
# virtualenv --version 
# virtualenv env --python=python3 | for creating environment
# pip3 freeze | Check what libraires are installed
# .\env\Script\activate | for using activate environement
# pip3 install pandas

import pandas as pd

df = pd.read_csv("./data/pokemon_data.csv")
# print(list(df.columns))

# print(df.head())
# print(df.tail())

# print(df.head(10))
# print(df.tail(10))

# axix = 0 # row -> index
# axix = 1 # column
get_specific_index = df.loc[10] # label of column [index/row, column]
print(get_specific_index)

get_all_names = df["Name"]
get_all_names = df.loc[:,'Name']

get_specific_index_column = df.loc[10, "Name"]

get_specific_multiple_rows_columns = df.loc[[10,23], ["Name", "Type 1"]]

# Column Filter
new_data= df.loc[df['Type 1'] == "Grass"]

# Multiple Column Filter
new_data= df.loc[(df['Type 1'] == "Grass") & (df["Type 2"] == "Flying")]

# Multple Column Filter with OR " | "
new_data= df.loc[(df['Type 1'] == "Grass") | (df["Type 1"] == "Fire")] #way 1
new_data= df[df["Type 1"].isin(["Grass", "Fire"])] #way 2

filter_coulmn_contains_str = df[df["Name"].str.contains("Mega")]
# print(len(filter_coulmn_contains_str))

# Count rows and columns
# print(df.shape)

# Sorting
# Sorting index
df = df.sort_index(axis=0)
print(df)

# Sorting columns
new_df = df.sort_index(axis=1, ascending=True) # Create another copy of data in memory
df.sort_index(axis=1, ascending=True, inplace=True) # update data in same ref
print(new_df)

# Sorting Values
df.sort_values(by=["Name"], ascending=True, inplace=True)
print(df)


