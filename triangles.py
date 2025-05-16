def create_triangle_1(n,character):
    for x in range(n):
        for y  in range(x+1):
            print(character,end='')
        print()
create_triangle_1(4,"%")

print("\n")

def create_triangle_2(n,character):
    for x in range(n):
        for y in range(n-x):
            print(character,end='')
        print()
create_triangle_2(4,"$")

print("\n")

def create_triangle_3(n,character):
    for x in range(0,n+1):
        for y  in range(0,n+1):
            if y<=n-x:
                print("",end="")
            else:
                print(character,end="")
        print()
create_triangle_3(4,"!")

print("\n")

def create_triangle_4(n,character):
    for x in range(n,0,-1):
        for y  in range(n+1):
            if y<=n-x:
                print("",end="")
            else:
                print(character,end="")
        print()
create_triangle_4(4,"^")

print("\n")

def create_triangle_5(n,character):
    for x in range(0,n-1):
        for y in range(x+1):
            if x>=n-y:
                print(character,end=" ")
            else:
                print(" ",end=" ")
        print()
create_triangle_5(8,"#")

print("\n")

def create_triangle_6(n,character):
    for x in range(n-1,0,-1):
        for y in range(x+1):
            if x>=n-y:          
                print(character,end=" ")
            else:
                print(" ",end=" "),
        print()
create_triangle_6(8,"?")
