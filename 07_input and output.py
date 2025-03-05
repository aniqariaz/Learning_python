# file input and output is used to open, read and close the file
# it has more more such as (r,w,a,x,t,+,b)

f=open("demo.txt", "r") 
data= f.read(5)
print(data)
print(type(data))
f.close()

