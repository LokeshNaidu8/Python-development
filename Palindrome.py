str="malayalam"
rev=""
for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]
    print(rev)
if(rev==str):
    print("its palindrome")
else:
    print("given string is not palindrome")