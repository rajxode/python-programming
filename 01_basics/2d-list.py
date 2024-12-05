
# 2d - list

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print a single element from matrix
print(matrix[0][0])

# print matrix row wise
for row in matrix:
    print(row)

# print each element of matrix one by one 
# nested for loop
for row in matrix:
    for col in row:
        print(col)

