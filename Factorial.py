
#Recursion
def fact(num):
    if(num==0):
        return 1
    else:
        return num*fact(num-1)
print("\nusing recursion ",fact(5),"\n")

#simple factorial

num=4
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Using for loop ",fact)