str1="hi I am string.\n And i am so happy." # strings are immutable..
print(str1)

# #concatenate
str1="happy"
str2="birthday"
sum = str1+str2
print(sum)

# #length of string

name="potter"
char=len(name)
print(char)

movie="harry" 
char2=len(movie)
print(char2)

sum =str1 +" "+ str2
print(sum)
print(len(sum))

# #indexing
str="my school"
char=str[2]
print(char)


# #slicing
str="city school"
print(str[1:4])

str="city school"
print(str[0:])

str="city school"
print(str[1:len(str)])

#string functions
str="i am learning python for programming"
print(str.endswith("ing"))

str="i am learning python for programming"
str=str.capitalize()
print(str)

str="i am learning python for programming"
print(str.replace("o","a"))

str="i am learning python for programming"
print(str.find("python"))

str="i am for learning python for programming"
print(str.count("for"))

# practice WAP to input user's first number and print its length..
str=input("my first name is:")
print(len(str))

#conditional statement
age=20
if(age<19):
    print("apply for lisence")
elif(age>=19):
    print("apply for id card")
print("code end")
# next
light="green"
if(light=="red"):
    print("stop the car")
elif(light=="green"):
    print("start the car")#condition is true  we only check elif state.. when if state.. is false
elif(light=="yellow"):
    print("look")
    print("code end")        

# #next use of else state..
light="pink"
if(light=="red"):
    print("stop the car")
elif(light=="green"):
    print("start the car")#condition true
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")    
    print("code is end")

#next when one of the state.. is true then else state.. will not run..
light="red"
if(light=="red"):
    print("stop the car")
elif(light=="green"):
    print("start the car")#condition true
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")    
print("code is end")

# #next
age=24
if(age>=19):
    print("can vote")
else:
    print("cannot vote")
    


# #next
num = 5
if(num>=3):
    print("greater than 3")#true both true run the first state.. when second is elif..
elif(num>=2):
    print("greater than 2")   # true 

# #next
num = 5
if(num>=3):
    print("greater than 3")#  when both true run the both state.. when second one also if...
if(num>=2):
    print("greater than 2") 

#next condition of marks and grades
marks = 76

if(marks >= 90):
    grade="A"
elif(marks >= 80 and marks < 90):
    grade="B"
elif(marks >= 70 and marks < 80):
    grade="C"
else:
    grade="D"

print("grade of students-> ",grade)

#we can take marks for input from the user

marks = int(input("enter students marks:"))

if(marks >= 90):
    grade="A"
elif(marks >= 80 and marks < 90):
    grade="B"
elif(marks >= 70 and marks < 80):
    grade="C"
else:
    grade="D"

print("grade of students-> ",grade)

#nesting
age = 36
if(age>= 18):
    if(age>=88):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")



# # example of nesting
#1.WAP to check if a num  entered by the user is odd or even
num = 14
rem = num % 2 # we can find the remainder
if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")

# #next
# #WAP to find the greatest of 3 num entered by the user
a=int(input("enter first num"))
b=int(input("enter second num"))
c=int(input("enter third num"))

if(a>b and a>c):
    print(" first large num")
elif(b>c and b>a):

    print("second large num")
else:
    print("third large num",c)
    
#to find the greatest of 4 num entered by the user...

a=int(input("enter first num"))
b=int(input("enter second num"))
c=int(input("enter third num"))
d=int(input("enter fourth num"))

if(a>b and a>c and a>d):
    print(" first is the largest num")
elif(b>c and b>d ):
    print("second is the largest num")
elif(c>d):
    print("third is the largest num")
else:
    print("fourth is the largest num",d)

# WAP to check if the num is the multiple of 7 or not...
num = int(input("enter multiple of :"))
if(num%7 == 0):#multiple of any number can be at that time when its remainder is 0. 
    print("multiple of 7")
else:
    print("not a multiple of 7")








    

    
    
    










