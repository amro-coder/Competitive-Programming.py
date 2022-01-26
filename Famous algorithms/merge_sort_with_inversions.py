def mergWithInversions(x,y):
    sorted=[]
    i=j=inversions=0
    while(True):
        if (i == len(x)):
            sorted.extend(y[j:])
            break
        if (j == len(y)):
            sorted.extend(x[i:])
            inversions+=(len(y)*(len(x)-i))
            break
        if (x[i] <= y[j]):
            sorted.append(x[i])
            i += 1
            inversions+=j
        else:
            sorted.append(y[j])
            j += 1
    return sorted,inversions

def mergSortWithInversions(x):
    if(len(x)<=1):
        return x,0
    y=x[len(x)//2:]
    x=x[:len(x)//2]
    x,leftInversions=mergSortWithInversions(x)
    y,rightInversions=mergSortWithInversions(y)
    sorted,splitInversions=mergWithInversions(x,y)
    return sorted,(leftInversions+rightInversions+splitInversions)

x=list(map(int,input().split()))
sorted,inversions=mergSortWithInversions(x)
print(inversions)
print(*sorted)