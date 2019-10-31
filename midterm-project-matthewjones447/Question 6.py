class record:
  def __init__(self, y, g, e, f, c, r):
    self.name = f
    self.gender = g
    self.ethnicity = e
    self.year = y
    self.count = c
    self.rank = r
  
def sortYear(rec):
    return rec.year
def six(allRankOne,entry):

  if (len(allRankOne) == 0):
      allRankOne.append(entry)
  
  if entry.ethnicity != allRankOne[-1].ethnicity:
    allRankOne.append(entry)
  
  

#----------------------------------------------------------------------------------------------

inputfile = open("Popular_Baby_Names.csv", "r")
    

allRankOne = []
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
   
  
       
    
allRankOne = allRankOne[1:]
allRankOne.sort(key = sortYear)
for rec in allRankOne:
    print(rec.year,rec.name, rec.ethnicity)
    
inputfile.close()
