def reverse_integer(n):
    b=0
    while n>0:
        a=n%10
        b=(b*10)+a
        n=int(n/10)
    return b