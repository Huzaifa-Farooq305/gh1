def factorial(x):
    y=1
    for a in range(1,x+1):
        y=y*a
    return y
print(factorial(6))

def factorial_second_method(n):
    f=1
    a=1
    while a<=n:
        f=f*a
        a=a+1
    return f
print(factorial_second_method(5))