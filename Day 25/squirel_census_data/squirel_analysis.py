import pandas as pd

df = pd.read_csv("Day 25/squirel_census_data/2018_squirrel_census.csv")
column_names = df.columns
print(column_names)

fur_color = df['Primary Fur Color']
print(fur_color.unique())

fur_count = fur_color.value_counts()

data_dict = fur_count.to_dict()
print(data_dict)

data = pd.DataFrame(data_dict.items(), columns=["fur_color", "count"])
data.to_csv("Day 25/squirel_census_data/squirrel_color_count.csv", index = False)