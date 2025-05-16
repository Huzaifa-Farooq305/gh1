def table(n,r):
    print("Tables"
        "\nFirst number you enter will be number for which table will be printed"
        "\nWhereas 2nd number will be range")
    n=int(n)
    for y in range(0,r+1):
        print(f"{n}*{y}={n*y}")
table(-9,100)