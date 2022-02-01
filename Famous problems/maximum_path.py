# Our next problem is to find a path from the upper-left corner to the lower-right
# corner of an n × n grid, such that we only move down and right. Each square
# contains a positive integer, and the path should be constructed so that the sum of
# the values along the path is as large as possible.
n=int(input())
x=[]
for _ in range(n):
    x.append(list(map(int,input().strip().split())))
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        dp[i][j]=max(dp[i+1][j],dp[i][j+1])+x[i][j]
print(dp[0][0])
