# with open("Day 25/weather_data.csv") as data_file:
#     data_list = data_file.readlines()
#     for data in data_list:
#         data_list_clean = data.strip()
#         print(data_list_clean)


import csv

with open("Day 25/weather_data.csv") as data_file:
    data_list = csv.reader(data_file)
    temperature = []
    for row in data_list:
        if row[1] != "temp":
            temperature.append(int(row[1]))
        print(row)
    print(temperature)


