def BinarySearch(seq,ele):
    seq.sort()
    print(seq)
    Low=0
    High=len(seq)-1
    Found=False
    while not Found and Low<=High:
        mid=(Low+High)//2
        if(seq[mid]==ele):
            print(f"You found out the item which is {ele} in index {mid}")
            Found=True
        elif(ele>seq[mid]):
            Low=mid+1
        elif(ele<seq[mid]):
            High=mid-1

    if(Found is False):
        print("nothing found")
BinarySearch([2,7,1,8,9,5,3],8)