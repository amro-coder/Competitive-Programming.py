def merg(x,y):
    sorted=[]
    i=0
    j=0
    while(True):
        if (i == len(x)):
            sorted.extend(y[j:])
            break
        if (j == len(y)):
            sorted.extend(x[i:])
            break
        if (x[i] <= y[j]):
            sorted.append(x[i])
            i += 1
        else:
            sorted.append(y[j])
            j += 1
    return sorted

def mergSort(x):
    if(len(x)<=1):
        return x
    right=x[len(x)//2:]
    left=x[:len(x)//2]
    return merg(mergSort(left),mergSort(right))
print(mergSort(list(map(int,input().split()))))