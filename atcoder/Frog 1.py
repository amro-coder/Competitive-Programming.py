# problem statement
# There are N stones, numbered 1,2,…,N. For each i (1≤i≤N), the height of Stone i is hi
# There is a frog who is initially on Stone 1. He will repeat the following action some number of times to reach Stone N:
# If the frog is currently on Stone i, jump to Stone i+1 or Stone i+2. Here, a cost of ∣hi−hj∣ is incurred, where j is the stone to land on.
# Find the minimum possible total cost incurred before the frog reaches Stone N.

# solution
import sys
input=sys.stdin.readline
n=int(input())
x=tuple(map(int,input().split()))
dp=[0]*n
dp[-2]=abs(x[-1]-x[-2])
for i in range(n-3,-1,-1):
    dp[i]=min(abs(x[i]-x[i+1])+dp[i+1],abs(x[i]-x[i+2])+dp[i+2])
print(dp[0])