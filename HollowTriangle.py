for i in range(1,6):
    for j in range(i):
        if(j==1 or i==5 or i==j):
            print("*",end=" ")
    print()