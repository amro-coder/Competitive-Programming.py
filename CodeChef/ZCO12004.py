import sys
input=sys.stdin.readline
n=int(input())
x=tuple(map(int,input().split()))
if(n<=2):
    print(min(x))
    exit()
dp=[0]*n
dp[-1]=min(x[-2],x[-1])
dp[-2]=min(x[-2],x[-3]+x[-1])
for i in range(n-3,-1,-1):
    dp[i]=min(x[i]+dp[i+2],x[i-1]+dp[i+1])
print(dp[0])