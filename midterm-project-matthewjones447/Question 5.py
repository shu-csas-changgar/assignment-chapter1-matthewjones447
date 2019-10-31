# Write a function the displays the year, count and rank of all WHITE NON HISPANIC males given the name David.
# Note: In 2012 the ethnicity is listed as WHITE NON HISP. Please take this into account in your code. (10 points)


def five(year, ethnicity, rank, first_name):
    if ethnicity.startswith("WHITE NON HISP") and first_name == "David":
        print(year, count, rank)


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
    rank = my_list[5][-1]

    five(year, ethnicity, rank, first_name)

inputfile.close()

