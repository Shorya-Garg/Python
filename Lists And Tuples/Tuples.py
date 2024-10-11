#Tuples are immutable.
a=() #Empty tuple
b=(1,) #Tuple with only one element needs comma.
c=(1,5,2,1,4,6,3,1)#Tuple with multiple elements
d=(1)# data type= integer
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#methods of tuple
print(c.count(1))  #count the number of times 1 appears in tuple c

print(c.index(4)) #return index of first occurrence of 4 in c

concatenated = b + c #To concatenate tuples
print(concatenated)



