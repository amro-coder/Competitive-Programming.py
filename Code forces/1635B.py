# You are given an array a of size n.
#  Each element in this array is an integer between 1 and 109.
# You can perform several operations to this array.
#  During an operation, you can replace an element in the array with any integer between 1 and 109.
# Output the minimum number of operations needed such that the resulting array doesn't contain any local maximums, and the resulting array after the operations.
# An element ai is a local maximum if it is strictly larger than both of its neighbors (that is, ai>ai−1 and ai>ai+1).
#  Since a1 and an have only one neighbor each, they will never be a local maximum.
#
#
#
#  solution:

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))+[10**9]
    ans=0
    for i in range(1,n-1):
        if(x[i-1]<x[i]>x[i+1]):
            ans+=1
            x[i+1]=max(x[i],x[i+2])
    print(ans)
    print(*x[:n])