
def binary_search(arr,n,find):
    start = 0
    end = n
    while start <= end:
        mid = int((end + start)/2)
        if(arr[mid] == find):
            return mid
        elif arr[mid] > find:
            end = mid - 1
        else:
            start = mid + 1
    return -1

arr = []
n = int(input("Size of the array: "))
print("Enter elements in ascending order")
for i in range(n):
    x = int(input("Enter element for " + str(i) + " : "))
    arr.append(x)

find = int(input("Enter element to search: "))
result = binary_search(arr, n-1,find)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: " + str(result))
