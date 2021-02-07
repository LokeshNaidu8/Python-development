n=int(input("Enter number of rows : "))
for col in range(1,n+1):
    for row in range(1,col+1):
        print("*",end="")
    print()