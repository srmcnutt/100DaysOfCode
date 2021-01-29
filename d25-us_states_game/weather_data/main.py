# things to remember
# data frame = table
# data series = row
# series directly accessible as a list where the column header is the key.
# we can select rows by placing a condition on a series

# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
# print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)

#     tempatures = []
#     for row in data:
#         tempatures.append(row[1])

# print(tempatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data)

temp_list = data["temp"].to_list()
print(temp_list)

length = len(temp_list)
totals = sum(temp_list)
avg = round(totals / length, 2)
print(avg)

print(data["temp"].mean())
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in row.
# we get rows by filtering a column on a condidtion
print(data[data.day == "Monday"])

# get day with maximum temp
print(data[data.temp == data.temp.max()])

# grab a field from a specific row (in this case condition)
monday = data[data.day == "Monday"]
print(monday.condition)

# create dataframe from from dict, write a csv file
data_dict = {"students": ["steve", "caroline", "diane"], "scores": [76, 75, 56]}

student_data = pandas.DataFrame(data_dict)
print(student_data)
data.to_csv("student_data.csv")