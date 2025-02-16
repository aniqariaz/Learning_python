# # # learn about lists that work like arrays...list are mutable...

marks1 = [94.5, 55.2, 78.9, 82.6, 90.1]
print(marks1)
print(type(marks1)) # datatype list

# # # access the element by indexing
marks1 = [94.5, 55.2, 78.9, 82.6, 90.1]
print(len(marks1))
print(marks1[0])
print(marks1[1])

# # # we can add diff.. type of data in list like float, char..
student = ["Aqsa", 94.8, "Karachi"]
print(student[0])
# element can change..
student[0] = "Aniqa"
print(student[0])

# # # slicing method in list..

marks = [45.7, 66.9, 92.1, 55.2, 78.3] # last index will not be included..
print(marks[1:4])
print(marks[0:])
print(marks[:4])
print(marks[-3:-1])

# # # list specific method..
list = [1, 2, 3]
list.append(4) #we can add a single element in the last..
print(list)

list = [2, 1, 3]
print(list.sort()) # return none because changes are consider in original list..
print(list)

list = [2, 1, 3]
list.append(4)
list.sort(reverse = True) #descending
print(list)

list = ["a", "b", "c"]
list.sort(reverse = True) #descending
print(list)

list = ["a", "b", "c", "e", "g"]
list.reverse()
print(list)

list = [1, 3, 2, 4]
list.insert(1,4)
print(list)

list = [1, 3, 2, 4]
list.remove(3)
print(list)

list = [1, 3, 2, 4]
list.pop(3) # pop the element by accessing the index..
print(list)

# # learn about tuple...tuples are immutable ...
tup = (1, 2, 3, 4)
print(tup)
print(type(tup))

tup=()
print(tup)
print(type(tup))

tup=(1,)
print(tup)
print(type(tup))

tup=(1, 2, 3, 4, 5)
print(tup[1:4])

#tuple methods ..
tup=(1, 2, 3, 4, 5)
print(tup.index(2))

tup=(1, 2, 3, 4, 5)
print(tup.count(2))

# # practice questions ...
# WAP to ask the the user to enter 3 fav... movies & store them in a list..
movie =[]
mov1 = input("enter 1st fav movies:")
mov2 = input("enter 2nd fav movie:")
mov3 = input("enter 3rd fav movie:")

movie.append(mov1)
movie.append(mov2)
movie.append(mov3) 

print(movie)

# # WAP that if a list is palindrome of elements...mean the list is same by copy and reverse it..
list1 = [1, 2, 3, 2, 1]
list2 =[1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

#next..    

list1 = [1, 2, 3, 2, 1]
list2 =[1, 2, 3]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindrome")

# Wap to the count num of student with the grade A..
tup = ("C", "D", "A", "A", "B")
print(tup.count("A"))

# SORT IT
LIST = ["C", "D", "A", "A", "B"]
LIST.sort()
print(LIST)















