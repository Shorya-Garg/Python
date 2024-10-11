marks={
    "John":90,
    "Emma":85,
    "Rohan":95,
    0: "Shorya"
}

# Accessing dictionary items
print(marks["John"])  # Output: 90

#a.item() method - return list of key-value tuple

print(marks.items())

# .keys - return list of keys of dict 

print(marks.keys())

# .values() - return list of values of dict 
print(marks.values())

# .update - update dict with given key-value pair

marks.update({"Rohan":99, "Shorya":100})
print(marks)

# .pop() - remove item with given key and return its value
marks.pop("Emma")

#.get() -return the value of specified key
print(marks.get("John"))
