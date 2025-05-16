def create_hollow_box(length, width,character):
    for x in range(length):
        for y in range(width):
            if x==0 or x==length-1 or y==0 or y==width-1:
                print(character,end='')
            else:
                print(' ',end='')
        print()
create_hollow_box(4,7,"+")