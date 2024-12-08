
def print_fib_series(num):
    if num == 0:
        print("invalid argument")
        return

    if num == 1:
        print(1)
        return
    
    series = "0 1"
    first = 0
    second = 1
    index = 3
    while index <= num:
        third = first + second
        first = second
        second = third
        series = series + " " + str(third)
        index += 1
    
    print(series)


n = int(input("Enter limit of fib series: "))
print_fib_series(n)