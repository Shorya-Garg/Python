#sort function
friends=['Apple','Dhruv',5,23.542,False,'Sarthak','Sajal']
print(friends)
#append method
friends.append("Shorya")
print(friends)
#sort method
l1=[1,34,2,1,4,314,134,61]
l1.sort() #work for integers
print(l1)

#reverse method
l1.reverse()
print(l1)

#insert method
l1.insert(2,100) #insert 100 at index 2
print(l1)

#pop method
print(l1.pop(2))#delete element at given index and return its value.
print(l1)

#remove method
l1.remove(100) #delete first occurrence of 100.
