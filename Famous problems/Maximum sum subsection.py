# Problem Statement:
#Given a sequence of integers, a subsection is a block of contiguous integers in the sequence.
# The task is to find the subsection whose sum is maximum.

# Solution
x=list(map(int,input().strip().split()))
n=len(x)
# both solutions are O(n)
maxSum=0
currentSum=0
for i in range(n):
    currentSum+=x[i]
    currentSum=max(0,currentSum)
    maxSum=max(maxSum,currentSum)
print("smart solution")
print(maxSum)
# dpSolution
dp=[0]*n
dp[-1]=x[-1]
for i in range(n-2,-1,-1):
    dp[i]=max(x[i],x[i]+dp[i+1])
print("dp solution")
print(max(*dp,0))