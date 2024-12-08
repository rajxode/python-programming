
def isPalindrome(str,length):
    i = 0
    j = length - 1
    mid = j / 2

    while( i<=mid and j>=mid):
        if(str[i] != str[j]):
            return False
        i+=1
        j-=1
    
    return True

str = input("Enter a word: ")
result = isPalindrome(str, len(str))

if result:
    print("Palindrome")
else:
    print("not a Palindrome")