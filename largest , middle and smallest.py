def comparison(a,b,c):
    if a<b<c:
        print(f"{c} is largest number, {b} is second largest number and {a} is smallest number")
    if a>b>c:
        print(f"{a} is largest number, {b} is second largest number and {c} is smallest number")
    if a>b<c:
        if a<c:
            print(f"{c} is largest number, {a} is second largest number and {b} is smallest number")
        elif c<a:
            print(f"{a} is largest number, {c} is second largest number and {b} is smallest number")
    if a<b>c:
        if a<c:
            print(f"{b} is largest number, {c} is second largest number and {a} is smallest number")
        else:
            print(f"{b} is largest number, {a} is second largest number and {c} is smallest number")
    if a==b==c:
        print(f"All values are equal i.e {a}")
    if a>b==c:
        print(f"{a} is largest no. other numbers have same value i.e. {b}")
    if a==b<c:
        print(f"{c} is largest no. other numbers have same value i.e. {b}")
    if a==c<b:
        print(f"{b} is largest no. other numbers have same value i.e. {a}")
    if a==b>c:
        print(f"First 2 values are largest numbers i.e. {a}, {c} is smallest number")
    if a<b==c:
        print(f"Last 2 values are largest numbers i.e {b}, {a} is smallest number")
    if a==c>b:
        print(f"1st value is equal to last value i.e. {a}, {b} is smallest number")
comparison(24333,595,241)