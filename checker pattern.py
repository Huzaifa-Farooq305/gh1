def create_checkers_pattern(l,w,c):
    for x in range(l):
        for y in range(w):
            print(c,end='')
        print()
        if x%2==0 :
            print(" ",end='')
    print()
create_checkers_pattern(4,8,"_")