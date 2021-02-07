num=5
a=5
for row in range(num,0,-1):
    for col in range(row,0,-1):
        print(a,end="")
    a-=1
    print()