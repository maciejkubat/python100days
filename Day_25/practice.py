# import csv
#
# with open('weather.csv') as file:
#      data = csv.reader(file)
#      temperatures = []
#      for index,row in enumerate(data):
#           if index >= 1:
#                temperatures.append(int(row[1]))
#      print(temperatures)

import pandas

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

data = pandas.read_csv('weather.csv')
temps = data["temp"].to_list()

avg = sum(temps) / len(temps)
print(avg)
max = data["temp"].max()
print(max)

monday = data[data.day == "Monday"]

print(data[data.temp == max])

temp = monday.temp.get(0)
temp_f = celsius_to_fahrenheit(temp)
print(f"{temp}C, {temp_f}F")