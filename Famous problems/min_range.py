import math
m=int(input())
x=tuple(map(int,input().split()))
n=math.floor(math.log(m-1,2))
dp=[[0]*m for _ in range(n+1)]
for i in range(m):
    dp[0][i]=x[i]
for i in range(1,n+1):
    for j in range(m):
        if(j+(2**i-1)<m):
            dp[i][j]=min(dp[i-1][j],dp[i-1][j+2**(i-1)])

for _ in range(int(input())):
    a,b=map(int,input().split())
    # index a and b are included
    length=b-a+1
    inc=math.floor(math.log(length,2))
    print(min(dp[inc][a],dp[inc][b-(2**inc-1)]))
