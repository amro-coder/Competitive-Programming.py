s1=input().strip()
s2=input().strip()
n=len(s1)
m=len(s2)
dp=[[0 for _ in range(m+1)] for __ in range(n+1)]
for i in range(1,n+1):
    dp[i][0]=i
for i in range(1,m+1):
    dp[0][i]=i
for i in range(1,n+1):
    for j in range(1,m+1):
        change_cost=1
        if(s1[i-1]==s2[j-1]):
            change_cost=0
        dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+change_cost)
# reconstructing solution:
# how to change s1 to be s2
ans=[]
i=n
j=m
while(i>0 and j>0):
    change_cost=1
    if(s1[i-1]==s2[j-1]):
        change_cost=0
    if(dp[i-1][j]+1==min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+change_cost)):
        ans.append(f"delete {s1[i-1]} in index {i}")
        i-=1
    if (dp[i][j-1]+1 == min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + change_cost)):
        ans.append(f"insert {s2[j-1]} after index {i}")
        j-=1
    else:
        if(change_cost==1):
            ans.append(f"change {s1[i-1]} in index {i} to {s2[j-1]}")
        i-=1
        j-=1
ans.reverse()
for i in ans:
    print(i)


print(dp[-1][-1])