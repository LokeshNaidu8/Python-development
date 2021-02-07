for row in range(5):
    for col in range(5):
        if(col+row==2 or col-row==2):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
