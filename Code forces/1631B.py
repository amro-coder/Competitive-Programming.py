# You are given an array a of n elements. You can apply the following operation to it any number of times:
#
# Select some subarray from a of even size 2k that begins at position l (1≤l≤l+2⋅k−1≤n, k≥1) and for each i between 0 and k−1 (inclusive),
# assign the value al+k+i to al+i.
# For example, if a=[2,1,3,4,5,3], then choose l=1 and k=2, applying this operation the array will become a=[3,4,3,4,5,3].
#
# Find the minimum number of operations (possibly zero) needed to make all the elements of the array equal.

#solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=tuple(map(int,input().split()))
    ans=0
    i=n-1
    value=x[i]
    while(i>0):
        if(x[i-1]==value):
            i-=1
        else:
            i-=(n-i)
            ans+=1
    print(ans)