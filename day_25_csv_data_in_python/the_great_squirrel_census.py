import pandas as pd

with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv", "r") as f:
    csv_data = pd.read_csv(f, usecols=["Primary Fur Color"], keep_default_na=False, skip_blank_lines=True)
    df = pd.DataFrame(csv_data)
squirrel_census = df.value_counts().rename_axis("Fur Color").reset_index(name="Count")
print(squirrel_census.iloc[0:3])


