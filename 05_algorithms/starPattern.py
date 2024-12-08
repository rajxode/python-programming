n = int(input("Enter number of rows: "))

'''
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
'''
for i in range(n):
    str = ""
    for j in range(i+1):
        str = str + "* "
    print(str)

'''
        *
       **
      ***
     ****
    *****
'''
for i in range(n):
    str = ""
    for k in range(n-i-1):
        str = str + " "
    for j in range(i+1):
        str = str + "*"
    print(str)


'''
     *
    ***
   *****
  *******
 *********
'''
for i in range(n):
    str = ""
    for k in range(n-i-1):
        str = str + " "
    for j in range( (2*i)+1):
        str = str + "*"
    print(str)