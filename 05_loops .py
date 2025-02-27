# while loops is used for the repeat instruction...when the condition is true
# then the print statement will run infinite time thats why it is important
# to make the condition false to stop the repeat instruction..It is commonly used when the number
# of iterations is not known..

while True :
    print("hello world") # it will print infinite time..

count = 1
while count<=5 :
    print("school") # it will print school 5 times..
    count += 1
print(count) # last count was 6..

i = 1
while i <= 100: # condition check..
    print("hurrah",i) # then work..
    i += 1
print(i) # last i is 101...


num = 1
while num <= 5:
    print( num) # print numbers...
    num += 1


num = 5
while num >= 1: # reverse counting...
    print("happy", num)
    num -= 1
print(num)

# practice question...
# print num from 1 to 100..
num = 1
while num <= 100:
    print("run")
    num += 1
print(num)
print("loop end")

# print num 100 to 1..
i = 100
while i >= 1: # condition check..
    print(i) # then work.. this is a stopping condition..
    i -= 1
print(i) # last count is 0.. 
print("loop end")

# print the multiplication table of a number n...

i = 1
while i <= 10:
    print(4*i)
    i += 1

# take the input of n from user...
n = int(input("enter number:"))
i = 1
while i <= 10:
    print(n*i)
    i += 1

# print the elements of the following list using a loop..
num=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]# index 9 and len 10
idx = 0
while idx < (len(num)):
    print(num[idx])
    idx += 1

# find the value of x in tuple.. and print it..
num =(1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )
x = 25
i = 0
while i < (len(num)):
    if(num[i] == x): 
        print("found in idx", i)
    else:
        print("finding")
    i += 1

# break keyword is used to terminate the loop when encountered...
num = 1
while num <= 5 :
    print(num)
    if(num == 4):
        break
    num += 1
print("end loop")
# next

num =(1, 4, 9, 16, 25, 36, 49, 64, 81, 100 )
x = 25
i = 0
while i < (len(num)):
    if(num[i] == x): 
        print("found in idx", i)
        break
    else:
        print("finding") # this will not run b/c of break keyword...
    i += 1

# continue keyword...i starts at 0 and increments by 1 each loop.
# When i == 3, the continue statement executes,
# skipping the print(i) statement.
# The loop moves to the next iteration with i = 4, continuing as usual.
i = 0
while i  < 5:
    if(i == 3):
        i += 1
        continue # skip
    print(i)
    i += 1
print("end loop")

# nextThe continue keyword in a while loop skips the
# rest of the current iteration and moves to the next iteration

i =1 # for odd num
while i < 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1
print("end loop")

i =1 # for even num
while i < 10:
    if(i%2  != 0):
        i += 1
        continue
    print(i)
    i += 1

# for loop is used sequential traversal for traversing list, tuple, and string..
num = [1, 2, 3, 4, 5]
for val in num:
    print(val) # it is used for print the value without access the index..    

veggies = ["tomato", "onion", "brinjal"]
for val in veggies:
    print(val)

tup =(1, 2, 3, 4, 5)
for ele in tup:
    print(ele)

str ="looking for something"
for char in str : # print in separately...
    print(char)    

# else is in for loop if the loop is complete then
# we can print anything in else condition...

str ="looking for something"
for char in str :
    if(char == "k"):
        print("k is found")
        break
    print(char) # after break the else condition will not work..
else:
    print("end")

# Practice question ..
# print the element of the following list using a loop...
num =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ]
for ele in num:
    print(ele)
else:
    print("end")

# search for a num x using tuple in loop..
num =(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36 ) #linear search
x = 36
idx=0
for ele in num:
    if(ele == x):
        print("36 is found",idx)
    idx += 1

# The range() function in Python generates a sequence of numbers.
# It is commonly used in loops. startswith 0 default , increment by 1
# and stop before specified number...
seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

seq = range(5)
for val in seq:# print 0 to 4..(start?, step? ,stop)
    print(val)

# we can also write..
for val in range(10):# stop
    print(val)

for i in range(2,10):
    print(i) # (start,stop)

for i in range(2,10, 2):# (start,stop, step)
    print(i)

for i in range(2, 100, 2):
    print(i) # for even number...


for i in range(1, 100, 2):
    print(i)#for odd num


# practice question...
# print 1 to 100 with for loop
for i in range(1, 101):
    print(i)

# print 100 to 1..for i in range(1, 101):
for i in range(100, 0, -1):
    print(i)

# multiplication of a table number n..
n = int(input("enter the num:"))
i = range(1, 11)
for i in range(1, 11):
    print(n*i)

# Pass statement is a  null statement that does nothing
# it is a place holder of future code
for i in range(10): #it will give the error so we can write pass
    #empty
    pass
print("nothing")

# practice question
#WAP to find the sum of first natural numbers (for loop)..
n =5
sum = 0
for i in range(1, n+1):
    sum += i 
print("total sum =",sum )

n =5
sum = 0
i = 1
while i<= n:
    sum += i
    i +=1
print("total sum =",sum )



#WAP a program to find the factorial of first natural numbers( loop)

n =5
fact = 1
i = 1
while i<= n:
    fact  *= i
    i +=1
print("factorial =",fact )









































