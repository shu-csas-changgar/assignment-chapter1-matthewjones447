class record:
  def __init__(self, y, g, e, f, c, r):
    self.name = f
    self.gender = g
    self.ethnicity = e
    self.year = y
    self.count = c
    self.rank = r
  
def sortCount(val):
  return val.count
  

   
def eight(current_entry,allAri):
  if current_entry.year == "2016"and current_entry.name == "Arianna"and current_entry.gender == "FEMALE":
    allAri.append(current_entry)
    
#----------------------------------------------------------------------------------------------

inputfile = open("Popular_Baby_Names.csv", "r")
    

allRankOne = []
userSearch = []
allAri = []
          

for line in inputfile:
    my_list = line.split(",")
    year = my_list[0]
    gender = my_list[1]
    ethnicity = my_list[2]
    first_name = my_list[3]
    count = my_list[4]
    rank = my_list[5]
    
    
    
    newEntry = record(year, gender, ethnicity, first_name, count, rank)
 
    eight(newEntry, allAri)
	   

       



allAri.sort(key = sortCount)

ariCount = 0
for rec in allAri:
  ariCount += int(rec.count)
  
print(ariCount)  
print(allAri[-1].ethnicity)

    
inputfile.close()

