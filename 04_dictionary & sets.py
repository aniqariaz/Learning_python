# learn about dictionary which are mutable and un ordered..it is a built in data type
# which is used to store data in key value pair ....

info = {
    "key" : "value",
    "name": "Aniqa riaz",
    "age" : 19,
    "subject":["math", "english", "sci"],
    "top" : ("dictionary"),
    
}
# print(type(info))
# print(info["name"])
# print(info["top"])
# print(info["subject"])

# # if we want to change the value... and add the value...
# info["name"] = "Aqsa riaz" # change the name..
# info["school"] = "city of knowledge" # add a value.. 
# print(info)

# null_dict ={}
# null_dict["name"]="Aniqa riaz"
# print(null_dict)

# #nested dictionary...
# student = {
#     "name": "Aniqa riaz",
#     "subject" :{
#         "physics":97,
#         "math": 80,
#         "com": 91,
#     }
# }
# print((student)["subject"])

# # dictionary method..

# student = {
#     "name": "Aniqa riaz",
#     "subject" :{
#         "physics":97,
#         "math": 80,
#         "com": 91,
#     }
# }
# print(list(student.keys()))# if we want to type cast in list
# print(len(student))

# print(list(student.values()))

# print(list(student.items()))

# print(student.get("name"))

# new_dict ={"city":"karachi"}
# student.update(new_dict)
# print(student)

# sets is the collection of unordered item the elements in the sets are immutable
# but the is set is mutable...

collection = {1, 2, 3, 4,4,4, "hello", "world", "world"}
print(collection)
print(type(collection))

null_set =set() # null set
print(null_set)

# Methods of sets...
null_set =set() # null set (in the sets we can,t store list and dictionaries)
null_set.add(2)
null_set.add(3)
null_set.add(4)
null_set.add("happy")
null_set.add("happy")
null_set.add((1, 2, 3, 4))
print(null_set)

# null_set.remove(3)
# print(null_set)

null_set.clear()
print(len(null_set))

collection ={"hello", "world", "learning", "python"}# it can remove a random value
collection.pop()
collection.pop()
print(collection)

# more important method union sets and intersection sets...
set1 ={1, 2, 3} #common elements will not be repeated...
set2 ={2,3,4,5}
print(set1.union(set2))

set1 ={1, 2, 3} #intersection include only common element...
set2 ={2,3,4,5}
print(set1.intersection(set2))

#practice questions....
#store following words meanining in a python dictionary...

python_dictionary ={
    "table" : ["a piece of furniture", "a list of facts and figure"],
    "cat" : "a small animal",
}
print(python_dictionary)

# to calulate the unique subjects we have to store it in the set....
set3 ={"python","java","c++","python","javascript","java", "python", "java", "c++","c"}
print(len(set3))







