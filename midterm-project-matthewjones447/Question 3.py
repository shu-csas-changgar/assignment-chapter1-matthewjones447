def three(year,first_name,gender,count, maxErics):
   
    if year == "2014" and first_name == "Eric" and gender == "MALE" and int(count) > maxErics:
        return True

    return False
    
#----------------------------------------------------------------------------------------------

inputfile = open("Popular_Baby_Names.csv", "r")
    
  
maxErics = 0
ericEthnicity = ""
for line in inputfile:
    my_list = line.split(",")
    year = my_list[0]
    gender = my_list[1]
    ethnicity = my_list[2]
    first_name = my_list[3]
    count = my_list[4]
    rank = my_list[5]
   
    #one(year, gender, ethnicity, first_name, count)
    #two(year,ethnicity,rank,first_name)  
    if (three(year, first_name, gender, count, maxErics) == True):
        maxErics = int(count)
        ericEthnicity = ethnicity
       
    
   
print(maxErics, ericEthnicity)
    
    
inputfile.close()
