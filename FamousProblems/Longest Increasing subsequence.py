# Problem Statement:
# Let s = a[1] a[2] ... a[n] be an unsorted sequence of numbers.
# A subsequence of s is one in which we drop some elements and retain the rest (so we need not pick up a contiguous segment, but we preserve the order of elements).
# For instance, a[1] a[3] a[n] is a subsequence.
# Problem: Find the (length of the) longest ascending subsequence.
# note this code solves the strictly increasing version

# Solution:
import sys
input=sys.stdin.readline
x=tuple(map(int,input().split()))
n=len(x)
# here is a direct dp solution
dp=[1]*n
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if(x[j]>x[i]):
            dp[i]=max(dp[i],1+dp[j])
ans=max(dp)
# constructing the solution
index=dp.index(ans)
solution=[x[index]]
i=index
count=ans-1
while(count>0):
    localMaxIndex=-1
    localMax=float('-inf')
    for j in range(i+1,n):
        if(x[j]>x[i]):
            if(dp[j]>localMax):
                localMaxIndex=j
                localMax=dp[j]
    i=localMaxIndex
    solution.append(x[i])
    count-=1
print("DP solution:")
print(ans)
print(solution)
# another way that works in o(nlog(n))!!
# just keep track of each best possible sequence last element
# then do binary search to know which last element to change
# here is the code
from bisect import bisect_left
biggest=max(x)+1
tailOfSequence=[biggest for _ in range(n)]
ans=0
for i in range(n):
    index=bisect_left(tailOfSequence,x[i],0,len(tailOfSequence)-1)
    tailOfSequence[index]=x[i]
    ans=max(ans,index)
print("smart solution:")
print(ans+1)



