import sys
input=sys.stdin.readline
n,k=map(int,input().split())
x=tuple(map(int,input().split()))
dp=[float('-inf')]*n
dp[0]=0
for i in range(1,n):
    for j in [i-1,i-2]:
        if(j>=0):
            dp[i]=max(dp[i],x[j]+dp[j])
for i in range(n-2,k-2,-1):
    for j in [i+1,i+2]:
        if(j<n):
            dp[i]=max(dp[i],x[j]+dp[j])
print(dp[k-1])