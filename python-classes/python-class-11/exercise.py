import pandas as pd

df = pd.read_csv("./data/employee_data.csv")

tail = df.tail()

row_15 = df.head(15)

row = df.loc[29]

all_column = df.loc[:, "Department"]

column = df.loc[4, "EducationLevel"]

columns = df.loc[4, ["Name", "EducationLevel"]]

columns_rows = df.loc[[7, 3], ["Name", "EducationLevel"]]

filter_HR_from_column = df.loc[df["Department"] == "HR"] 
filter_HR_from_column = df[df["Department"].isin(["HR"])]


filter_HR_Gender_from_column = df.loc[(df["Department"] == "HR") & (df["Gender"] == "Male")] 

filter_Bachelor_PHD_from_column = df[df["EducationLevel"].isin(["Bachelor", "PhD"])]
filter_Bachelor_PHD_from_column = df.loc[(df["EducationLevel"] == "Bachelor") | (df["EducationLevel"] == "PhD")]

filter_coulmn_contains_str = df[df["Department"].str.contains("IT")]
filter_coulmn_contains_str = df[~df["Department"].str.contains("IT")]


# df.sort_values(by=["EducationLevel"], ascending=True, inplace=True)
# df.sort_values(by=["EducationLevel"], ascending=True, inplace=True)

df.loc[16, "Name"] = "Hamza"
change_name = df.loc[16, "Name"]
df.loc[:, "Name"] = "Hamza" #way 1
df["Name"] = "Hamza" #way 2

df.loc[:, "Department"] = df.loc[:, "Department"].str.lower()  #way 1
df["Department"] = df["Department"].str.lower()  #way 2

change_name = df.loc[:, "Department"]

new_df = df.groupby(['Department', 'Gender']).count()["Name"]
new_df = df.groupby(['Department']).sum()["Salary"]
new_df = df.groupby(['Department', "Gender"]).sum()["Salary"]
print(new_df)

