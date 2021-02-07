
num=153
ognum=num
result=0

while(num>0):
    i=num%10
    result=result+(i*i*i)
    num=int(num/10)
a=int(result)
print(a)
print(num)
print(ognum)