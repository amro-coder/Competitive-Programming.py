# problem Statement:
# In a grid of size R x C, you need to find the number of paths from the top-left to the bottom-right.
# You may only move 1 block to the right or one block down in each step.
# You may not go through any blocked intersections (given), and you may take at most d consecutive steps in the same direction. R, C <= 300.

# solution
import sys
input=sys.stdin.readline
r,c,d=map(int,input().split())
grid=[]
for _ in range(r):
    grid.append(tuple(map(int,input().split())))
dp=[[[[0]*(d+1),[0]*(d+1)] for __ in range(c+1)] for _ in range(r+1)]
for i in range(d+1):
    dp[-2][-2][0][i]=dp[-2][-2][1][i]=1
for i in range(r-1,-1,-1):
    for j in range(c-1,-1,-1):
        if(i==r-1 and j==c-1) or grid[i][j]==0:
            continue
        for moves in range(1,d+1):
            # dir =0 means right
            dp[i][j][0][moves]=dp[i][j+1][0][moves-1]+dp[i+1][j][1][d-1]
            dp[i][j][0][0]=dp[i+1][j][1][d-1]
            dp[i][j][1][moves]=dp[i][j+1][0][d-1]+dp[i+1][j][1][moves-1]
            dp[i][j][1][0]=dp[i][j+1][0][d-1]
print(max(dp[0][0][0][d],dp[0][0][1][d])%20011)