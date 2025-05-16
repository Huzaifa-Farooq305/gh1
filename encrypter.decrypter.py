from digitp_pickup import pickup_digit
def encrypt(n):
    if n>=1000 or n<=9999:
        d4=pickup_digit(n,1)
        d3=pickup_digit(n,2)
        d2=pickup_digit(n,3)
        d1=pickup_digit(n,4)
        d1=(d1+7)%10
        d2=(d2+7)%10
        d3=(d3+7)%10
        d4=(d4+7)%10
        d1,d2,d3,d4=d3,d4,d1,d2
        b=d1*1000+d2*100+d3*10+d4
    return b
print(encrypt(627))

def decrypt(n):
    if n>=1000 or n<=9999:
        d4=pickup_digit(n,1)
        d3=pickup_digit(n,2)
        d2=pickup_digit(n,3)
        d1=pickup_digit(n,4)
        d1=(d1-7)%10
        d2=(d2-7)%10
        d3=(d3-7)%10
        d4=(d4-7)%10
        d1,d2,d3,d4=d3,d4,d1,d2
        b=d1*1000+d2*100+d3*10+d4
    return b
print(decrypt(9473))