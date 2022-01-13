# problem:
# yor are given x1,x2,y1,y2 such that x1<=x2 and y1<=y2.
# you are allowed to move down or right or diagonally down.
# meaning that from (x,y) you can go to (x+1,y) or (x,y+1) or (x+1,y+1)
# your task is to find the number of ways you can reach (x2,y2).
# Input
# Input starts with an integer (T<=50) which denotes the number of test case.
# Each test case consists four integer x1, y1, x2, y2 (0<=x1<=x2<=100000 and 0<=y1<=y2<=100000)

# direct DP solution ( would result in TLE)
# import sys
# input=sys.stdin.readline
# for _ in range(int(input())):
#     x1,y1,x2,y2=map(int,input().split())
#     dp=[[0]*(y2-y1+2) for _ in range(x2-x1+2)]
#     dp[-1][-1]=1
#     for i in range(x2-x1,-1,-1):
#         for j in range(y2-y1,-1,-1):
#             dp[i][j]=dp[i+1][j]+dp[i][j+1]+dp[i+1][j+1]
#     print(dp[0][0])

# better solution takes 10^5 operation
mod=10**9+7
def factorialAndModualrInverse(n,prime):
    modInv = [1] * (n + 1)
    factorial = [1] * (n + 1)
    modInvFactorial=[1]*(n+1)
    for i in range(2, n + 1):
        modInv[i] = modInv[prime % i] * (prime - prime // i) % prime
        factorial[i] = (factorial[i - 1] * i) % prime
        modInvFactorial[i] = (modInvFactorial[i - 1] * modInv[i]) % prime
    return factorial,modInvFactorial
factorial,modInvFactorial=factorialAndModualrInverse(100000,mod)
def getComb(n,r):
    if(n<r) or (n==0 and r==0):
        return 0
    return (factorial[n]*modInvFactorial[r]*modInvFactorial[n-r])%mod


import sys
input=sys.stdin.readline
for _ in range(int(input())):
    ans=0
    x1, y1, x2, y2 = map(int, input().split())
    diffx=x2-x1
    diffy=y2-y1
    for i in range(min(diffx,diffy)+1):
        ans+=getComb(diffx+diffy-i,min(diffx,diffy)-i)*getComb(diffx+diffy-i-(min(diffx,diffy)-i),i)
    print(ans)



