def cf(n,x):
    l=[]
    if n<x:
        y=n
    else:
        y=x
    for b in range(1,y+1):
        if n%b==0 and x%b==0:
            l.append(b)
    return l 
 

def hcf(n,x):  

    return max(cf(n,x))
print(hcf(243,366))

