def sum_of_factors(n):
    sum=0
    for a in range(1,n):
        if n%a==0:
            sum+=a
    return sum

def isperfect(x):
    return x==sum_of_factors(x)
print(isperfect(6))