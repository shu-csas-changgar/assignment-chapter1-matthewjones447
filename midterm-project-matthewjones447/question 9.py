class record:
  def __init__(self, y, g, e, f, c, r):
    self.name = f
    self.gender = g
    self.ethnicity = e
    self.year = y
    self.count = c
    self.rank = r
  
  
def six(allRankOne,entry):

  if (len(allRankOne) == 0):
      allRankOne.append(entry)
  
  if entry.ethnicity != allRankOne[-1].ethnicity:
    allRankOne.append(entry)
  
def get_name_by_ethnicity(user_year,user_ethnicity, user_gender,user_rank):
    inputfile = open("Popular_Baby_Names.csv", "r")
  
    for line in inputfile:
        my_list = line.split(",")
        year = my_list[0]
        gender = my_list[1]
        ethnicity = my_list[2]
        name = my_list[3]
        count = my_list[4]
        rank = my_list[5]
    
        if user_year == year  and int(user_rank) == int(rank) and user_gender == gender and user_ethnicity == ethnicity:
            inputfile.close()
            return name

    inputfile.close()
    return ""



#----------------------------------------------------------------------------------------------


    

allRankOne = []
userSearch = []

user_year = input("Enter a year: ") 
user_ethnicity = input("Enter a ethnicity: ")
user_gender = input("Enter a gender: ") 
user_rank = input("Enter a rank: ")

print(get_name_by_ethnicity(user_year, user_ethnicity, user_gender, user_rank))


