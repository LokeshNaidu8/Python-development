

def quickSort(l1):
    if(len(l1)<=1):
        return l1
    else:
        pivot=l1.pop()

    preList=[]
    postList=[]

    for i in l1:
        if(i<pivot):
            preList.append(i)
        else:
            postList.append(i)
    return quickSort(preList)+[pivot]+quickSort(postList)

print(quickSort([3,5,1,2,9,7]))
