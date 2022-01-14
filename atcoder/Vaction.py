# problem statement
# Taro's summer vacation starts tomorrow, and he has decided to make plans for it now.
# The vacation consists of N days. For each i (1≤i≤N), Taro will choose one of the following activities and do it on the i-th day:
# A: Swim in the sea. Gain ai points of happiness.
# B: Catch bugs in the mountains. Gain bi points of happiness.
# C: Do homework at home. Gain ci points of happiness.
# As Taro gets bored easily, he cannot do the same activities for two or more consecutive days.
# Find the maximum possible total points of happiness that Taro gains.
# solution
import sys
input=sys.stdin.readline
n=int(input())
x=[]
for _ in range(n):
    x.append(tuple(map(int,input().split())))
dp=[[float('inf'),float('inf'),float('inf')] for _ in range(n)]
dp[-1]=x[-1]
for i in range(n-2,-1,-1):
    dp[i][0]=x[i][0]+max(dp[i+1][1],dp[i+1][2])
    dp[i][1]=x[i][1]+max(dp[i+1][0],dp[i+1][2])
    dp[i][2]=x[i][2]+max(dp[i+1][0],dp[i+1][1])
print(max(dp[0]))