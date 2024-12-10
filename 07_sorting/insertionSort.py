def insertion_sort(arr,n):
    for i in range(1,n):
        max = i
        j = i - 1
        print(max,j)
        while j>=0:
            if arr[max] < arr[j]:
                temp = arr[j]
                arr[j] = arr[max]
                arr[max] = temp
                max = j
            j -= 1
    print(arr)

n = int(input("Enter the size: "))
arr = []

for i in range(n):
    x = int(input("Enter element at "+str(i)+" : "))
    arr.append(x)

insertion_sort(arr,n)
print(arr)