import pandas as pd

# with open(r"Day_25\weather_data.csv") as data_file:
#     data = data_file.readlines()

# for row in data:
#     print(data[row])

# import csv

# with open("Day_25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pd.read_csv("Day_25\weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()
# avg = sum(temp_list) / len(temp_list)
# print(round(avg))
# print(round(data["temp"].mean())) #return average value of temperatures
# print(data["temp"].max()) #return maximum value of temperatures

# Get Data in Columns
# print(data.condition) # is the abreviation of the line below 👇
# print(data["condition"]) 

# Get Data in Row

# print(data[data.temp])
# print(data[data.temp == data.temp.max()])

# def fahrenheit(celsius):
#     """Convert the celsius parameter to fahrenheit"""
#     conv_value = celsius * 9/5 + 32
#     return conv_value

# monday = data[data.day == "Monday"]
# monday_temp_fah = fahrenheit(monday.temp)
# print(monday_temp_fah)

# Create a dataframe from scratch

# data_dict = {
#     "students": ["Amy","John","Angela"],
#     "scores": [76, 56, 65]
# }
# data2 = pd.DataFrame(data_dict)
# data2.to_csv("Day_25\data2_file.csv")

data = pd.read_csv(r"Day_25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]
}

squirrel_data = pd.DataFrame(data_dict)
squirrel_data.to_csv("Day_25\squirrel_numbers.csv")

print(pd.read_csv("Day_25\squirrel_numbers.csv"))



