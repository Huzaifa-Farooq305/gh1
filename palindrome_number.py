from order_reverser import reverse_integer
def ispalindrome(x):
    ispalindromenumber=True
    if reverse_integer(x)==x:
        ispalindromenumber=True
    else:
        ispalindromenumber=False
    return ispalindromenumber
print(ispalindrome(141))