#While loop => check condition then execution of statement.
i=1
while(i<6):
    print(i)
    i=i+1
    
# Print list content using while loop
l=[1,"Harry",False,"Thos",45,24.3,"End"]
while(len(l)):
    print(l.pop()) # pop() function is used to remove the last element from the list.
#or
"""i=0
while(i<len(l)):
    print(l[i])
    i++"""