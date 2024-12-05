
# creating a simple function
def say_hello():
    print("Hello user")

say_hello()

# function with parameter
def say_hello2(name):
    print("Hello " + name)

say_hello2("World")

#function with multiple params
def say_hello3(name,age):
    print("Hello " + name + " ,you are " + str(age) + " years old")

say_hello3("VenuGopal Iyer", 56)

# function with return statement
def cube (num):
    return num * num * num

result = cube(3)
print("Cube of 3 is: " + str(result))