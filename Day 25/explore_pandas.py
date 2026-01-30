import pandas as pd
import numpy as np

df_weather = pd.read_csv("Day 25/weather_data.csv")
# The entire table is a type = Dataframe
print(type(df_weather))

# A single columnd is a type = Series
print(df_weather["temp"])
print(type(df_weather["temp"]))

# Printing column names
print(df_weather.columns)

# Pandas data frame to dictionary
df_dict = df_weather.to_dict()
print(df_dict)

# Pandas series (column) to list
temp_list = df_weather["temp"].to_list()
temp_list = df_weather["temp"].to_list()
print(temp_list)

avg = sum(temp_list)/len(temp_list)
print((avg))

# Average directly in pandas
print(df_weather["temp"].mean())
# Max in pandas
max_temp= df_weather["temp"].max()

print(df_weather[df_weather.day == "Monday"])
print(df_weather[df_weather["day"] == "Monday"])


# Which row of data has the highest temperature ? 
print(df_weather[df_weather["temp"] == max_temp])

# Creating a dataframe from scratch
data_dict = { 
    "students" : ["Amy", "Mark", "Marija", "Peter", "Natalia"],
    "scores" : [21,18,30,30,6] 
    }

data = pd.DataFrame(data_dict)
data.to_csv("Day 25/example_new_dataframe.csv", index = False)