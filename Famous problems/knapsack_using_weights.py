import sys
input=sys.stdin.readline
n,w=map(int,input().split())
value=[]
weight=[]
for _ in range(n):
    w1,v1=map(int,input().split())
    weight.append(w1)
    value.append(v1)
max_value=n*max(value)
dp=[float('inf')]*(max_value+1)
dp[0]=0
for i in range(n):
    for j in range(max_value,value[i]-1,-1):
        dp[j]=min(dp[j],dp[j-value[i]]+weight[i])
for i in range(max_value,-1,-1):
    if(dp[i]<=w):
        ans=i
        break
print(ans)
# reconstruct solution
solution=[]
i=ans
while(i>0):
    for j in range(n):
        if(value[j]<=i and (dp[i]==dp[i-value[j]]+weight[j])):
            solution.append((weight[j],value[j]))
            i-=value[j]
            break
print(*solution)
