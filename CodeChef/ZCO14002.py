import sys
input=sys.stdin.readline
n=int(input())
x=tuple(map(int,input().split()))
if(n<3):
    print(0)
    exit()
dp=[0]*n
dp[-3]=min(x[-3],x[-2],x[-1])
for index in range(n-4,-1,-1):
    dp[index]=min(x[index]+dp[index+1],x[index+1]+dp[index+2],x[index+2]+dp[index+3])
print(dp[0])