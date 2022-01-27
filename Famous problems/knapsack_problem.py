n,w=map(int,input().split())
weights=[0]
values=[0]
for _ in range(n):
    weight,value=map(int,input().split())
    values.append(value)
    weights.append(weight)
dp=[[0 for _ in range(w+1)] for __ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,w+1):
        if(weights[i]>j):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weights[i]]+values[i])
print(dp[n][w])
# reconstruct solution
knapsack=[]
i=n
j=w
while(i>0 and j>0):
    if(dp[i][j]!=dp[i-1][j]):
        knapsack.append((values[i], weights[i]))
        j -= weights[i]
    i-=1
print(*knapsack)












