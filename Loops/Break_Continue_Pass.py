# Break statement is used to terminate(exit) the loop.
for i in range(6):
    if(i==4):
        break
    print(i)

# Continue is used to skip an iteration
for i in range(6):
    if(i==4):
        continue
    print(i)  # This will print 0,1,2,3,5

# Pass is used to do nothing. for future work

for i in range(645):# hume iss loop pe baad me kaam karna hai par if we leave it as it is it will give error so use pass.
    pass


i=0
while(i<45):
    print(i)
    i+=1