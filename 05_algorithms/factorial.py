
# using iterative approach
def find_factorial(num):
    fact = 1
    while num > 0:
        fact = fact * num
        num -= 1
    
    return fact

# using recursion
def recursive_find_fact(num):
    if num == 1:
        return 1
    
    return num * recursive_find_fact( num - 1)


num = int(input("Enter a number: "))
result = find_factorial(num)
result1 = recursive_find_fact(num)

print("Factorial of " + str(num) + " is: " + str(result))