n1=0
n2=1
print(f"{n1} {n2}",end=" ")
for i in range(2,10):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3