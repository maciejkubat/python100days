import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census.csv')

colours = data["Primary Fur Color"]
colour_count = colours.value_counts()

print(colour_count)

colour_count.to_csv('colour_count.csv')