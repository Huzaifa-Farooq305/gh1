def fac(n):
    c=[]
    for a in range(1,n+1):
        if n%a==0:
            c.append(a)
    return c
print(fac(26))
