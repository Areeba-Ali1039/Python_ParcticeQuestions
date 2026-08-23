dates = [1982 , 1980 , 1973 , 2000]
i = 0 
year = dates[i]
while  year!= 1973:
    print(year)
    i += 1
    year = dates[i]
    
   
print("it took ", i , "iteration to find the year 1973")
# Ques1
# name = input("Enter Your name: ")
# print(f"Good Afternoon, {name}")
# Ques2
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# print (letter.replace("<|Name|>","Areeba").replace("<|Date|>","25/07/2026"))
#Ques3
sentence = "Areeba is  a good girl"
print(sentence.find("  "))
print(sentence.replace("  "," "))