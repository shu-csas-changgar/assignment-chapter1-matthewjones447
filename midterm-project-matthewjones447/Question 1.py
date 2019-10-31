import csv


def one(Year, Gender, Ethni, First, count):  
  if Year == "2013" and Gender == "FEMALE" and Ethni == "HISPANIC" and First == "Zoey": 
  	print(count)
  
  






#----------------------------------------------------------------------------------------------

inputfile = open("Popular_Baby_Names.csv", "r")
    
  

for line in inputfile:
    my_list = line.split(",")
    year = my_list[0]
    gender = my_list[1]
    ethnicity = my_list[2]
    first_name = my_list[3]
   
    one(year, gender, ethnicity, first_name, my_list[4])
      

    
    
inputfile.close()

