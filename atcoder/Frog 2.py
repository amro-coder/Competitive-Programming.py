# problem statement
# There are N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is hi.
# There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:
# If the frog is currently on Stone i, jump to one of the following: Stone i+1,i+2,…,i+K. Here, a cost of ∣hi−hj∣ is incurred, where j is the stone to land on.
# Find the minimum possible total cost incurred before the frog reaches Stone N.

# solution
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
x=tuple(map(int,input().split()))
dp=[float('inf')]*n
dp[-1]=0
for i in range(n-1,-1,-1):
    for j in range(i+1,min(i+k+1,n)):
        dp[i]=min(dp[i],abs(x[i]-x[j])+dp[j])
print(dp[0])