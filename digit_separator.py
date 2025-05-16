def separate_digits(n):
    x=""
    while n>0:
        m=n%10
        n=int(n/10)
        x=f"{m}    {x}"
    return x
print(separate_digits(1234))

