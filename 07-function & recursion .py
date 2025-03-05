# function is a block of statement which perform specific task..
def cal_sum(a, b): # take input
    sum=a+b
    print(sum)
    return sum# give output

cal_sum(2, 5) # call function
# # some work
cal_sum(4, 7) # it decrease redundancy b/c
                #the function is already perform to sum the values..

#function definition..
def calc_sum (a, b):# parameters
    return a+b

sum=calc_sum(666, 55)# function call
print(sum)

def print_hello(): # no parameters
    print("hello") # so there is no return value..
print_hello()
print_hello()
print_hello()
print_hello()

# average of 3 numbers
def avg(a, b, c):
    sum = a +b +c
    avg =sum/3
    print(avg)
    return avg

# avg(2, 3,4)

#default parameters..
#when we dont want to pass any arguments then parameters allow us to use default values..
def cal_prod(a=1, b=1):# give default value from the last
    print(a*b)
    return  a*b

cal_prod()


def cal_prod(a, b=6):# give default value from the last
    print(a*b)
    return  a*b

cal_prod(1) # 1 will store in the a...

# Practice question 
#WAF to print the length of a list (list is a parameter)

cities =["karachi", "islamabad", "lahore", "peshawar" ]
cartoons =["mr bean", "tom and jerry", "teen titans", "charlie", "oggy and the cock"]

def print_len(list):
    print (len(list))

print_len(cities)
print_len(cartoons)

# WAF to print the element of a list in a single line...


cities =["karachi", "islamabad", "lahore", "peshawar" ]
cartoons =["mr bean", "tom and jerry", "teen titans", "charlie", "oggy and the cock"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cartoons)

#WAF to find a factorial of n (n in parameters)

def cal_fact(n):
    fact =1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)

#WAF to convert usd into pkr..

def convertor(usd_val):
    pkr_val=usd_val*83
    print(usd_val,"usd =" , pkr_val,"pkr" )
convertor(2)


def num(n):
    if(n%2 != 0):
        print("odd")
    else:
        print("even")
        

num(8)

# example...

def num_input():
    num1=int(input("enter number:"))
    if(num1%2 != 0):
        print("odd")
    else:
        print("even")
        

num_input()

# RECURSIVE FUNCTION 
def show(n):
    if(n ==0): #n=0 then then n=0 will not print and all other value print..
        return
    print(n)
    show(n-1) #5-1=4, 4-1=3, 3-1=2, 2-1=1, 


show(5)

#Calculate sum of first n natural number by recursive function,,
def cal_sum(n):
    if(n == 0 ):
        return 
    return cal_sum(n-1)+n
print(cal_sum(5))