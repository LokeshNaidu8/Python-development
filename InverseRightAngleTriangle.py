n=int(input("enter number of rows: "))

for col in range(n,0,-1):
    for spaces in range(n-col):
        print("",end=" ")
    for row in range(col):
        print("*", end="")
    print()