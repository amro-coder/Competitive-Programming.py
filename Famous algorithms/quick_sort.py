import random
# if we dont choose a random piviot , we can get a O(n**2) running time
def partition(l,r):
    i=l+1
    for j in range(i,r):
        if (x[j] < x[l]):
            x[i], x[j] = x[j], x[i]
            i += 1
    x[l], x[i - 1] = x[i - 1], x[l]
    return i-1
def QuickSort(l,r):
    if(l>=r):
        return
    s=random.randrange(l,r)# random piviot
    x[s],x[l]=x[l],x[s]
    p=partition(l,r)
    QuickSort(l,p)
    QuickSort(p+1,r)
x=list(map(int,input().split()))
QuickSort(0,len(x))
print(*x)

