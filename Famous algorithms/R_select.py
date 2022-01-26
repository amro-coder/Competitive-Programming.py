import random
# same idea as quick sort but we either call the right half or left half
def partition(l,r):
    i=l+1
    for j in range(i,r):
        if (x[j] < x[l]):
            x[i], x[j] = x[j], x[i]
            i += 1
    x[l], x[i - 1] = x[i - 1], x[l]
    return i-1
def RSeclect(l,r):
    s=random.randrange(l,r)
    x[s],x[l]=x[l],x[s]
    p=partition(l,r)
    if(p==pos):
        return x[pos]
    if(pos>p):
        return RSeclect(p+1,r)
    return RSeclect(l,p)
x=list(map(int,input().split()))
pos= int(input())
print(RSeclect(0,len(x)))
