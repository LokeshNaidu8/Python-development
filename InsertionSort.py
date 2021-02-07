def insertionSort(seq):
    for i in range(1,len(seq)):
        selected=seq[i]
        while seq[i-1]>selected and i>0:
            seq[i],seq[i-1]=seq[i-1],seq[i]
            i=i-1
    return seq


print(insertionSort([4,2,9,1,7]))