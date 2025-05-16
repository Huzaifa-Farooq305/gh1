def isprime(n):
    isPrime=True
    if n==1 or n==0:
        isPrime=False
    for a in range(2,int(n/2)):
        if n%a==0:
            isPrime=False
            break
    return isPrime
print(isprime(0))