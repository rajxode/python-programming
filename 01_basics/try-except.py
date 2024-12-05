
# for handling errors
num = int(input("Enter a number: "))
print(num)

'''
    the above code will give error if
    user enter some value other than a number
    to handle this error we can use
    try except block
'''

try:
    num2 = int(input("Enter a number: "))
    print(num2)
except:
    # this except block will handle all types of error
    # we can use multiple excepts for different type of error
    print("Invalid input")


try:
    num3 = int(input("Enter a number: "))
    print(num3)
    answer = num3 / 0
except ZeroDivisionError:
    # will handle error of division by zero
    print("Divide by zero")
except ValueError:
    # handle error of wrong input
    # input other than number in this case
    print("Invalid input")
