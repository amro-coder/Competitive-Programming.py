# problem statement:
# In short you need to find 2 increasing sub sequence, one goes to right another one goes to left.
# But they can't have common cells.
# What is the maximum number of cells you can visit?

# solution
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=tuple(map(int,input().split()))
    dp=[[[float('-inf')]*n for _ in range(n)] for __ in range(n)]
    dp[-1][-1][-1]=1

    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            for k in range(i+1,n):
                if(x[i]<x[j]):
                    dp[i][i][k] = max(dp[i][i][k], dp[i + 1][j][k]+1)
                if(x[i]>x[k]):
                    dp[i][j][i]= max(dp[i][j][i],dp[i+1][j][k]+1)

                dp[i][j][k]=dp[i+1][j][k]

                if(i==k):
                    dp[i][i][k] = max(dp[i][i][k], 1)
                else:
                    dp[i][i][k] = max(dp[i][i][k], 2)
                if(i==j):
                    dp[i][j][i] = max(dp[i][j][i], 1)
                else:
                    dp[i][j][i] = max(dp[i][j][i], 2)
    ans=0
    for i in range(n):
        ans=max(ans,max(dp[0][i]))
    print(ans)







