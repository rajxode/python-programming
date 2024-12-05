
# getting a string input
name = input("Enter your name: ")
print("Hello " + name + " !")

# getting an integer input from user
# by default python convert the incoming input into string values
age = input("Enter your age: ")
print("Hello " + name + " your are " +age + " years old !!")


num1 = input("Enter first number: ")
num2 = input ("Enter second value: ")

# converting the string number input to float for performing mathematical operations
result = float(num1) + float(num2)

print("Sum of " + num1 + " + " + num2 + " is: " + str(result))