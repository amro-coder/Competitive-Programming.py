#Problem Statement
# Counting paths in a grid:
# You have a rectangular grid of points with n rows and n columns. You start at the top left corner.
# At each step, you can either go down to the next point in the same column or right to the next point in the same row.
# How many such paths are there from the top left corner to the bottom right corner?
# What if some points are deleted (that is, no path can go through these points)?

# Solution:
from collections import defaultdict
n,m=map(int,input().split())
k=int(input())
blocked=[]
for ___ in range(k):
    blocked.append(tuple(map(int,input().split())))
dp=[[0 for _ in range(m)] for __ in range(n)]
dp[0][0]=1
blocked= defaultdict(bool,{i:True for i in blocked})
for i in range(n):
    for j in range(m):
        if (not blocked[(i, j)]):
            if(i-1>=0):
                dp[i][j]+=dp[i-1][j]
            if(j-1>=0):
                dp[i][j]+=dp[i][j-1]
print(dp[-1][-1])
# or if there is no blocked points then can be calculated using the combinations!
# how many ways to choose the right moves of the total moves
# n=2 m=5 => total moves=(2-1) + (5-1)=5=> ans= C(5,1)=C(5,4)
# import math
# print(math.comb(n+m-2,n-1))