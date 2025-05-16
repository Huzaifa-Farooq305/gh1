from calc import display_menu
from arr_ops import quit_program
from arr_ops import welcome_message
welcome_message("Calculator")
display_menu()
o=0
while o>=1 or o<=6:

    o=int(input("\nEnter a number between 1 and 6: "))
    if o==1:
        print("You have chosen addition")
        x =int(input("Operand 1: "))
        y=int(input( "Operand 2:"))
        print(f"{x}+{y}={x+y}")

    elif o==2:
        print("You have chosen subraction")
        x=int(input("Operand 1: "))
        y=int(input( "Operand 2:"))
        print(f"{x}-{y}={x-y}")

    elif o==3:
        print("You have chosen Multiplication")
        x=int(input("Operand 1: "))
        y=int(input( "Operand 2:"))
        print(f"{x}*{y}={x*y}")
        
    elif o==4:
        print("You have chosen division")
        x=int(input("Operand 1 (Numerator): "))
        y=int(input( "Operand 2 (Denominator):"))
        print(f"{x}/{y}={x/y}")

    elif o==5:
        print("You have chosen modulus")
        x=int(input("Operand 1: "))
        y=int(input("Operand 2:"))
        print(f"{x}%{y}={x%y}")

    elif o==6:
        print("You have chosen exponentiation")
        x=int(input("Operand 1 (number): "))
        y=int(input( "Operand 2 (power):"))
        print(f"{x}**{y}={x**y}")
    else:
        q=input("Are you sure you want to quit(yes/no): ")
        if q=="yes":
            quit_program()
            break
        elif q=="no":
            display_menu()
            continue   