def multiple(a,b):
    ismultiple=True
    c=a%b
    if c==0:
        ismultiple=True
    else:
        ismultiple=False
    return ismultiple
print(multiple(75,5))