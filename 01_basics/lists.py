
# list: collection of elements
peoples = ["Aditi", "Nisha", "Munni", "Sheetal"]
numbers = [1,2,3,4,5]

# print whole list
print(peoples)

# print element at a specific position
# first element
print(peoples[0])
# last element
print(peoples[-1])
# some specific position element
print(peoples[2])

# print elements is a given range
# print from index 1 to last
print(peoples[1:])
# print from index 1 to index 2 (exclude the index 3)
print(peoples[1:3])

# udpate list value 
peoples[3] = "Gullu: Taxi driver"
print(peoples)

# list in-built functions
# adding two list
peoples.extend(numbers)
print(peoples)
# append value at the end of list
peoples.append("Bunty")
print(peoples)
# insert new element in list at a specific position
peoples.insert(2,"MG Gandhi")
print(peoples)
# remove
peoples.remove("Aditi")
print(peoples)
# remove all
peoples.clear()
print(peoples)

peoples = ["Bunty", "MG Gandhi", "Gullu", "Bawla", "MG Gandhi", "Taxi Driver"]
print(peoples)
# pop() remove the last element
peoples.pop()
print(peoples)
# index of element
print(peoples.index("Bunty"))
# count occurence of an element
print(peoples.count("MG Gandhi"))
# sort list
peoples.sort()
print(peoples)
# reverse 
peoples.reverse()
print(peoples)
# copy list
newPeople = peoples.copy()
print(newPeople)