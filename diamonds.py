from triangles import create_triangle_5
from triangles import create_triangle_6
def create_filled_diamond(n,character):
    create_triangle_5(n,character)
    create_triangle_6(n,character)
create_filled_diamond(8,"*")
def create_hollow_diamond(n,character):
    for x in range(0,n-1):
        for y in range(x+1):
            if y==n-x or x==y and y>=n-x:
                print(character,end=" ")
            else:
                print(" ",end=" ")
        print()
    for x in range(n-1,0,-1):
        for y in range(x+1):
            if y==n-x or x==y and y>=n-x :          
                print(character,end=" ")
            else:
                print(" ",end=" "),
        print()
create_hollow_diamond(8,"*")