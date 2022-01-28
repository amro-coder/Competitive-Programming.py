import sys
input=sys.stdin.readline
n,w=map(int,input().split())
values=[0]
weights=[0]
for _ in range(n):
    w1,v1=map(int,input().split())
    weights.append(w1)
    values.append(v1)
max_value=n*max(values)
dp=[[float('inf')]*(max_value+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=0
for i in range(1,n+1):
    for j in range(1,max_value+1):
        dp[i][j]=dp[i-1][j]
        if(j-values[i]>=0):
            dp[i][j]=min(dp[i][j],weights[i]+dp[i-1][j-values[i]])

for i in range(max_value,-1,-1):
    if(dp[n][i]<=w):
        ans=i
        break
print(ans)