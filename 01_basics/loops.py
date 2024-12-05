
# a variable for checking condition
i = 1

# loop until the condition is true
# loop while the value of i is less than or equals to 10
while i <= 10:
    print("2 * " + str(i) + " = " , str( (2 * i)))
    # increment value of i
    i+= 1

print("While Loop over !!")

# ===================== For Loop =====================

# loop over each character in the string
for character in "Hello World":
    print(character)

# list
peoples = ["Bunty", "Gullu", "Baburao", "DeviPrashad", "Kabira"]
# loop over each element in the above list
for person in peoples:
    print(person)

# loop till the provide range (excluding 10)
for j in range(10):
    print(j)

# loop between the provided range (3-9, excluding 10)
for k in range(3,10):
    print(k)

# loop from start to end of list length
for m in range(len(peoples)):
    # print element at each index
    print(peoples[m])
