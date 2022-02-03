def doseValueExist(value,array):
    n=len(array)
    i=0
    j=0
    total=0
    while(True):
        if(total==value):
            return f"sum found from index {i+1} to index {j}"
        if(j>=n or i>=n):
            return "sum not found"
        if(total<value):
            total+=array[j]
            j+=1
        else:
            total-=array[i]
            i+=1

target=int(input())
x=tuple(map(int,input().split()))
print(doseValueExist(target,x))