n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    for j in range(n-1-i):
        if(x[j]>x[j+1]):
            x[j],x[j+1]=x[j+1],x[j]
print(*x)