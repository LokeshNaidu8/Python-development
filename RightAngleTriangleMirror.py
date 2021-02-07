n=int(input("Enter number of rows : "))
for col in range(1,n+1):
    for row in range(n-col):
        print("",end=" ")
    for sym in range(col):
        print("*",end="")
    print()