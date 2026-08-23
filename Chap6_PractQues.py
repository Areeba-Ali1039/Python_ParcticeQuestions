# Ques 1
# no1 = int(input("Enter a number : "))
# no2 = int(input("Enter a number : "))
# no3 = int(input("Enter a number : "))
# no4 = int(input("Enter a number : "))
# if (no1 > (no2 and no3 and no4)) :
    # print(no1,"is greater than all other 4 numbers ")
# elif (no2 > (no3 and no1 and no4)):
    # print(no2,"is greater than all other 4 numbers")
# elif (no3 > (no1 and no2 and no4)):
    # print(no3,"is greater than all other 4 numbers")
# elif (no4 > (no1 and no2 and no3)):
    # print(no4,"is greater than all other 4 numbers")
# else:
    # print("the number is invalid")
#Ques2
# sub1 = int (input("Enter marks of subject 1 :"))
# sub2 = int (input("Enter marks of subject 2 :"))
# sub3 = int (input("Enter marks of subject 3 :"))
# total_percentage = (100*(sub1+sub2+sub3))/300
# if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    # print("You have successfully passed the examination by",total_percentage,"%.Congrats!!")
# else:
    # print("You have successfully failed the examination by",total_percentage,"%.Better luck next year!!")

#Quest 3(kinda wrong bcz need a whole sentence for this to be spam)
# comment = input("Write a comment : ")
# if(comment=="Make  a lot of money" or "buy now" or"subscribe this" or "click this"):
    # print("Spam comment detected",comment)
# else:
    # print(comment)
# or 2nd method using in (good methos bcz these phrases in any sentence are considered spam)
# p1 = "Make a lot of money"
# p2 = "click this"
# p3 = "buy now"
# p4 = "subscribe this"
# comment = input("Write a comment : ")
# if ((p1 in comment ) or (p2 in comment) or (p3 in comment) or (p4 in comment)):
    # print("Spam message detected",comment)
# else:
    # print("this is not a spam comment",comment)
# Ques 4
# username = input("Enter Your name : ")
# if (len(username)<10):
    # print("Characters of this name is",len(username),"which is less than 10")
# else:
    # print("characters of this name is greater than 10")
# Ques 5
# names = ['Areeba','Ali','Arsal','reeb','areeb']
# name = input("Enter Your name : ")
# if name in names:
    # print("Name found !!")
# else:
    # print("Name not found!!")
# 
# Ques 6
# marks = int (input("Enter Your marks : "))
# if (marks >=90 and marks <=100):
    # grade = "Ex"
# elif(marks >=80 and marks <=90):
    # grade = "A"
# elif(marks >=70 and marks <=80):
    # grade = "B"
# elif(marks >=60 and marks <=70):
    # grade = "C"
# elif(marks >=50 and marks <=60):
    # grade = "D"
# else:
    # grade = "F"
# 
# print("Your grade is : ", grade)
#Quest 7
p1 = "Harry" 
msg = input("Write something : ")
if (p1.lower() in msg.lower() ):
    print("This post is about Harry")
else:
    print("This post is not about harry")