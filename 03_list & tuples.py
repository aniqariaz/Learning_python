# learn about lists that work like arrays...

marks1 = [94.5, 55.2, 78.9, 82.6, 90.1]
print(marks1)
print(type(marks1)) # datatype list

# access the element by indexing
marks1 = [94.5, 55.2, 78.9, 82.6, 90.1]
print(len(marks1))
print(marks1[0])
print(marks1[1])

# we can add diff.. type of data in list like float, char..
student = ["Aqsa", 94.8, "Karachi"]
print(student[0])
# element can change..
student[0] = "Aniqa"
print(student[0])

# slicing method in list..

marks = [45.7, 66.9, 92.1, 55.2, 78.3] # last index will not be included..
print(marks[1:4])
print(marks[0:])
print(marks[:4])
print(marks[-3:-1])

# list specific method..
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








