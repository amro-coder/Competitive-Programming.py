# Problem Statement:
# Tiling problem:
# Problem: You are given a grid of size n×2 and n tiles of size 2×1
# In how many different ways can you tile the grid such that the entire grid is covered and no tiles overlap. (The tiles look identical to each other).
# Two ways of tiling are different based on whether the tiles are placed horizontally or vertically.
# Solution:
n=int(input())
# recursive approach
# def rec(n):
#     if(n<=1):
#         return 1
#     return rec(n-1)+rec(n-2)
# print(rec(n))
# now lets use DP
#base case
dp=[1,1]
for i in range(2,n+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[n])