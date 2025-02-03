print("hello world" ) #how python give the input

print("my name is Aniqa","my age is 19")

print(45)
print(67+45)

# # # learn about variables
name="Aniqa Riaz"
age=19
price=59.8

print(name)
print(age)
print(price)

print("my name is:",name)
print("my age is:",age)

# # #value as a variable
age2=age
print(age2)

# # #data type
print(type(name))
print(type(age))
print(type(price))

age=None
old=False


print(type(old))
print(type(age))

# print sum
a=6
b=4
diff=a-b
print(diff)

# # arithmetic operator
a=4
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)#remainder
print(a**b)#a^b

#relational operator
a=50
b=40
print(a==b)#False
print(a!=b)#True
print(a>=b)#True
print(a>b)#True
print(a<=b)#False
print(a<b)#False

#assignment operators
num=10
num=num+10
print("num:",num)

num=10
num*=5
print(num)

num=10
num+=5
print(num)#15

num=10
num/=5
print(num)#2

num=10
num%=5
print(num)#0

#logical operators
a=50
b=40
print(not False)
print(not True)
print(not(a>b))

# and operator
val1=False
val2=False
print("and operator:",val1 and val2)

#or operator

val1=False
val2=True
print("and operator:",val1 and val2)
print("or operator:",val1 or val2)
print("or operator:",a==b or a>b)

# #type conversion 
a=2
b=5.25
sum=a+b
print(sum)

# #type casting
a=int("2")
b=5.25
print(type(a))
sum=a+b
print(sum)

a=3.14
a=str(a)
print(type(a))

#input
name=input("my name is:")
print("welcome",name)
print(type(name))

val1=input("enter some values:")
print(type(val1),val1)

name=int(input("enter your age:"))
print("my age is:",name)
print(type(name))

name=float(input("enter your age:"))
print("my age is:",name)
print(type(name))

#practice

name=input("enter your name:")
age=int(input("enter your age:"))
marks=int(input("enter your marks:"))

print("my name is",name)
print("my age is",age)
print("my total marks are",marks)

print(type(name))
print(type(age))
print(type(marks))

#write a program to input two numbers and print their sum
first=int(input("enter first"))
second=int(input("enter second"))
print("sum",first+second)


a=2
b=6
sum=a+b
input("enter two numbers:")
print("sum of two numbers are",sum)

#wap to input side of sqr and print its area
sid1=int(input("enter square side:"))

print("area of sqr",sid1*sid1)

#next example
a=float(input("first float num:"))
b=float(input("second float num:"))
print("average num=",a+b/2)

#enter two num if greater print true if not false

a=float(input("first float num:"))
b=float(input("second float num:"))
print(a>=b)



