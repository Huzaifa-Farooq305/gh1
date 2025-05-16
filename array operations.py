from arr_ops import fill_list
from arr_ops import calculate_sum
from arr_ops import calculate_average
from arr_ops import display_menu
from arr_ops import validate
from arr_ops import invalid_message
from arr_ops import error_message
from arr_ops import welcome_message
from arr_ops import quit_program

option=0
arr=[]
welcome_message("Array Operations Program")
while option!=6:
    display_menu()
    option=int(input("Enter a number between 1 and 6: "))
    if option==6:
        quit_program()
        break
    elif option>6 or option<1:
        invalid_message(6,1)
        continue
    if option==1:
        print("Press 9999 to stop")
        print(fill_list(arr))
    else:
        if validate(arr):
            if option==2:
                print(f"Sum of the list is {calculate_sum(arr)}")
            if option==3:
                print(f"Average of the list is {calculate_average(arr)}")
            if option==4:
                print(f"Minimun number of the list is {min(arr)}")
            if option==5:
                print(f"Maximum number of the list is {max(arr)}")
        else:
            error_message()