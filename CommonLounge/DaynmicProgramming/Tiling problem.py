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