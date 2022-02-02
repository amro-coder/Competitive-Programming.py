n,w=map(int,input().split())
weight=[]
value=[]
for _ in range(n):
    w1,v1=map(int,input().split())
    value.append(v1)
    weight.append(w1)
dp=[0 for _ in range(w+1)]
for i in range(n):
    for j in range(w,weight[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
print(dp[w])
# reconstruct solution
solution=[]
visited=[False]*n
i=w
while(i>0):
    for j in range(n):
        if(weight[j]<=i and (not visited[j]) and (dp[i]==dp[i-weight[j]]+value[j])):
            solution.append((weight[j],value[j]))
            i-=weight[j]
            visited[j]=True
            break
    else:
        i-=1
print(*solution)












