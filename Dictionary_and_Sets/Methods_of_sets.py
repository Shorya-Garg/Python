s=set()
# add method
s.add(3)
print(s)

#.clear
s.clear()
print(s)
s.add(5)
s.add(3)
s.add('Shorya')

#.copy
c=s.copy()
print(c)

#length
print(len(s))

#remove
s.remove(3)
print(s)

#pop
s.pop() #remove random element from set / dont use it
print(s)

#union
s1={1,2,3}
s2={3,4,5}
print(s1.union(s2)) #output will be {1,2,3,4,5}

print(s1.intersection(s2)) #output will be {3}

print(s1.difference(s2)) #output will be {1,2}

print(s1.symmetric_difference(s2)) #output will be {1,2,4,5}  => (s1 U s2) - (s1 intersection 2)

