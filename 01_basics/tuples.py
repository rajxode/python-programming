
# tuples ( are immutable => value cannot be changed )
coordinates = (4, 5, 6)

# coordinates[1] = 7   // not possible because of immutable nature of tuples

print(coordinates)
print(coordinates[0])
print(coordinates[1])

# list ( mutable => value can be changed after declaration ) 
coord = [4,5,6]
coord[2] = 7

print(coord)
print(coord[0])
print(coord[2])

# list of tuples
# each element of the following list is a tuple
coord_list = [(1,2),(3,4),(5,6),(7,8)]
print(coord_list)
print(coord_list[0])

# here we are updating the list not the tuple therefore it is possible
coord_list[0] = (9,10)
print(coord_list)


# here we are trying to update the value of the tuple at the index = 1, and it is not possible
# coord_list[1][0] = 11