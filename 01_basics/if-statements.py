
# simple if statement
is_deviPrashad = True
# if condition true run
if is_deviPrashad:
    print("Star Garage")


# if-else condition
is_deviPrashad = False
if is_deviPrashad:
    # if true
    print("Star Garage")
else:
    # if false
    print("Star Fisheries")


# if-else using 'or' operator
is_kabira = True
is_shyam = True
# if either one is true
if is_kabira or is_shyam:
    print("Kabira speaking either kabira or shyam")
else:
    # if both are false
    print("Wrong number !!!")


# if-else using 'and' operators
is_aditi = True
is_munni = False
# if both are true
if is_aditi and is_munni:
    print("Aditi hi munni hai")
else:
    # if either one is false
    print("either not munni or not aditi or both(Nisha)")


# if-else-if ladder using "and" oeprator
is_tall = True
is_male = False
# if both true
if is_tall and is_male:
    print("You are a tall male")
# if first true and second false 
elif is_tall and not(is_male):
    print("You are tall but not male")
# if first false and second true 
elif not(is_tall) and is_male:
    print("You are a short male")
# if both are false
else:
    print("You are not a male and not tall")


# using comparison operators
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(1,2,3))