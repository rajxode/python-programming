def selection_sort(arr,n):
    for i in range(n-1):
        min = i
        k = i + 1
        for j in range(k,n):
            if arr[min] > arr[j]:
                min = j
        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp

n = int(input("Enter the size: "))
arr = []

for i in range(n):
    x = int(input("Enter element at "+str(i)+" : "))
    arr.append(x)

selection_sort(arr,n)
print(arr)