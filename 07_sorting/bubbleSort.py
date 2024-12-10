def bubble_sort(arr,n):
    for j in range(n-1):
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i+1] = temp
        n -= 1

n = int(input("Enter the size: "))
arr = []

for i in range(n):
    x = int(input("Enter element at "+str(i)+" : "))
    arr.append(x)

bubble_sort(arr,n)
print(arr)
        