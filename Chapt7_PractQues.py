# quick quizz --->Write a program to print the content of a list using while loops.
# list = ['areeba' , ' ali' , 'areeb' , 'reeba', 1 , 5.6 , 78 ]
# i = 0
# while (i < (len(list))):
    # print("in the list at index ",i,"the value is ",list[i])
    # i += 1
# print("Program successfully executed") 
#Ques 1 
#
#  no = int(input("Enter a number for which you want the table : "))
# for i in range(0,11):
    # print(no,'x',i,'=',i * no)
    #print(f" {no} x {i}= {n*i}")-->  through f string we can print variables also directly

# Quest 2
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l:
    # if (name.startswith('S')):
        # print(f"Hello {name} !!")
    # else:
        # print("Go to hell bcz ur name doesnt start with S")

#Quest 3
#
# no = int(input("Enter a number for which you want the table : "))
# i = 0
# while(i<11):
#   print(f"{no} x {i}= {no*i}")
#   i += 1
#Ques 4
#
#  no = int(input("Enter a no: "))
# for i in range(2, no):
    # if (no%i) == 0):
        # print("Not prime Number")
        # break
# else:
    # print("Prime Number")
#Quest 5
#
# no = int(input("Enter  a no: "))
# i =1
# sum = 0
# while(i < no):
    # sum += i
    # i +=1
# print("Sum : ",sum)
#Quest 6
#5! = 5 x 4 x 3 x 2 x 1
n = int(input("Enter a  no : "))
product= 1
for i in range (1, n+1):
 product *= i
   
print(f"The factorial of {n} is {product}")


#Quest 7
'''
for n = 3
  *
 ***
*****
'''
# n = int(input("Enter a no : "))
# for i in range (1,n+1):   
    # print(" "*(n-i),end = "")
    # print('*'*(2*i-1), end = "")
    # print("")
#Quest 8 
# n = 3
# for i in range(1,n+1):
    # print(i*'*')
#Ques 9
# n = int(input("Enter a no : "))
# for i in range (1,n+1):
    # if(i == 1 or i == n):
        # print('*'*n , end = '')
    # else:
        # print('*',end = '')
        # print(" "*(n-2),end="")
        # print('*',end ='')
    # print("")

#Quest 10
# n = int(input("Enter a no : "))
#print("The Table is given as : ")
# for i in range(1,11):
    # print(f"{n} x {11-i} = { n*(11-i)}")