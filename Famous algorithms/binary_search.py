def binSearch(x,target):
    low=0
    high=len(x)-1
    while(low<=high):
        mid=(low+high)//2
        if(x[mid]==target):
            return mid
        if(target>x[mid]):
            low=mid+1
        else:
            high=mid-1
    # return low (if you want the index of the bigger element)
    # return high (if you want the index of the smaller element)
    return -1
x=tuple(map(int,input().split()))
target=int(input())
print(binSearch(x,target))