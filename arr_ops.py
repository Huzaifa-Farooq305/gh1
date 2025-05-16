def fill_list(arr=[]):
    n=0
    while n!=9999:
        n=int(input("Enter a number: "))
        if n!=9999:
            arr.append(n)
    return arr


def calculate_sum(arr=[]):
    s=0
    for a in arr:
        s+=a
    return s

def calculate_average(arr=[]):
    return calculate_sum(arr)/len(arr)

def maximum(n):
    max=0
    for item in n:
        if item>max:
            max=item
    return max

def display_menu():
    print("\nPress any of the options to proceed:"
        "\n1-Fill Array"
        "\n2-Find Sum"
        "\n3-Find Average"
        "\n4-Find Minimum Value"
        "\n5-Find Maximum Value"
        "\n6-Exit")

def validate(arr=[]):
    return len (arr)>0

def exit_message():
    z="\n-----EXITING-----"
    z+="\nTHE PROGRAM HAS BEEN EXITED."
    print(z)


def invalid_message(f,l):
    print(f"[INVALID INPUT!]: Values Greater than {f} or smaller than {l} can not be entered.")

def error_message():
    print("{ERROR}: You must fill an array if you want any other option to work")

def welcome_message(b):
    print(f"Welcome to {b}")

def quit_program():
        z="\n-----EXITING-----"
        z+="\nTHE PROGRAM HAS BEEN EXITED."
        print(z)


def calculate_difference(arr=[]):
    d=0
    arr[1]=arr[1]*-1
    for a in arr:
        d-=a
    return d

def calculate_prod(arr=[]):
    p=0
    for a in arr:
        p*=a
    return p