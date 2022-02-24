import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    total=sum(a)+sum(b)
    total_sqr=0
    min_sum=0
    for i in range(n):
        total_sqr+=a[i]**2+b[i]**2
        min_sum+=min(a[i],b[i])

    dp=1
    for i in range(n):
        dp|= dp<<abs(a[i]-b[i])

    ans=float("inf")
    for i in range(10001):
        if(dp>>i) & 1:
            ans=min(ans,((n-2)*total_sqr)+((min_sum+i)**2)+(total-(min_sum+i))**2)
    print(ans)