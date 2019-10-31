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
  
def seven(user_year,user_rank, currentRecord, userSearch):
  if user_year == currentRecord.year  and int(user_rank) == int(currentRecord.rank):
    userSearch.append(currentRecord)

#----------------------------------------------------------------------------------------------

inputfile = open("Popular_Baby_Names.csv", "r")
    

allRankOne = []
userSearch = []

user_year = input("Enter a year: ") 
user_rank = input("Enter a rank: ")
for line in inputfile:
    my_list = line.split(",")
    year = my_list[0]
    gender = my_list[1]
    ethnicity = my_list[2]
    first_name = my_list[3]
    count = my_list[4]
    rank = my_list[5]
    
    
    
    newEntry = record(year, gender, ethnicity, first_name, count, rank)
    six(allRankOne, newEntry)
    seven(user_year, user_rank, newEntry, userSearch)
   
  
       
    
allRankOne = allRankOne[1:]

if (len(userSearch) == 0):
    print("No names found")

for rec in userSearch:
  print(rec.name, rec.gender,rec.count)

for rec in allRankOne:
    print(rec.name, rec.ethnicity)
    
inputfile.close()



#--------------------------------------------------------------------------------
