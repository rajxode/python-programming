
def linear_search(arr, find):
    for i in arr:
        if i == find:
            return arr.index(i)
        
    return -1

arr = []
n = int(input("Enter size of array: "))
for i in range(n):
    x = int(input("Enter element at index " + str(i) +": "))
    arr.append(x)

find = int(input("Enter the element to find: "))
result = linear_search(arr,find)

if result == -1:
    print("Element not found")
else:
    print("Element found at index: " + str(result))