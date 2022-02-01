# problem statement:
# 1 - calculate the minimum number of coins to reach a given sum
# 2 - how many different ways to get the given sum note we can use the coins any number of times

# 1- minumim number of coins to reach a given sum
total=int(input())
coins=list(map(int,input().strip().split()))
dp=[total for _ in range(total+1)]
dp[0]=0
for i in coins:
    for j in range(total+1):
        if (j-i) >= 0:
            dp[j]=min(dp[j],dp[j-i]+1)
print(dp[total])
# reconstruct solution:
ans=[]
sum=total
while(sum>0):
    coin=(total+1,-1)
    for i in coins:
        if(sum-i>=0):
            coin=min(coin,(dp[sum-i]+1,i))
    sum-=coin[1]
    ans.append(coin[1])
print(*ans)
# 2- number of ways to reach a given sum
dp=[0 for _ in range(total+1)]
dp[0]=1
for i in coins:
    for j in range(total+1):
        if (j-i) >= 0:
            dp[j]+=dp[j-i]
print(dp[total])






