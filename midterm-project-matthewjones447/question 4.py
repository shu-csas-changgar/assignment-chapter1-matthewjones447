##Write a function that displays which ethnicities had the same number 1 ranked name for females
# in the year 2014 (10 points)

import csv

top_names = []


def four(year, ethnicity, rank, first_name):
    if year == "2014" and int(rank) == 1:
        top_names.append([ethnicity, first_name])
    return top_names


# ----------------------------------------------------------------------------------------------

inputfile = open("Popular_Baby_Names.csv", "r")

zoeys = 0
for line in inputfile:
    my_list = line.split(",")
    year = my_list[0]
    gender = my_list[1]
    ethnicity = my_list[2]
    first_name = my_list[3]
    count = my_list[4]
    rank = my_list[5]

    four(year, ethnicity, rank, first_name) # populate the top_names with ethnicity and the name

names = []

# make a list of just the names so that we can get the unique names
for name in top_names:
    names.append(name[1])

unique_names = list(set(names)) # set function drops any duplicates

for unique_name in unique_names:
    if names.count(unique_name) > 1: # is there more than 1 of the name
        for j, name in enumerate(names):
            if name == unique_name:
                print(top_names[j][0], top_names[j][1])
inputfile.close()

