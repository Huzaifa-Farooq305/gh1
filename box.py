def create_box(length, width,character):
    for x in range(length):
        for y in range(width):
            print(character,end='')
        print()
create_box(3,5,"/")

def create_hollow_box(length, width,character):
    for x in range(length):
        for y in range(width):
            if x==0 or x==length-1 or y==0 or y==width-1:
                print(character,end='')
            else:
                print(' ',end='')
        print()
create_hollow_box(4,7,"+")

def create_checkers_pattern(l,w,c):
    for x in range(l):
        for y in range(w):
            print(c,end='')
        print()
        if x%2==0 :
            print(" ",end='')
    print()
create_checkers_pattern(4,8,"_")