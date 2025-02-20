# learn about dictionary which are mutable and un ordered..it is a built in data type
# which is used to store data in key value pair ....

info = {
    "key" : "value",
    "name": "Aniqa riaz",
    "age" : 19,
    "subject":["math", "english", "sci"],
    "top" : ("dictionary"),
    
}
print(type(info))
print(info["name"])
print(info["top"])
print(info["subject"])

# if we want to change the value... and add the value...
info["name"] = "Aqsa riaz" # change the name..
info["school"] = "city of knowledge" # add a value.. 
print(info)

null_dict ={}
null_dict["name"]="Aniqa riaz"
print(null_dict)

#nested dictionary...
student = {
    "name": "Aniqa riaz",
    "subject" :{
        "physics":97,
        "math": 80,
        "com": 91,
    }
}
print((student)["subject"])

# dictionary method..

student = {
    "name": "Aniqa riaz",
    "subject" :{
        "physics":97,
        "math": 80,
        "com": 91,
    }
}
print(list(student.keys()))# if we want to type cast in list
print(len(student))

print(list(student.values()))

print(list(student.items()))

print(student.get("name"))

new_dict ={"city":"karachi"}
student.update(new_dict)
print(student)



