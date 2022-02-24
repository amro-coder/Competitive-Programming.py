# Let there be an array b1,b2,…,bk. Let there be a partition of this array into segments [l1;r1],[l2;r2],…,[lc;rc], where l1=1, rc=k, and for any 2≤i≤c holds that ri−1+1=li.
# In other words, each element of the array belongs to exactly one segment.
#
# Let's define the cost of a partition as
# c+∑i=1cmex({bli,bli+1,…,bri}),
# where mex of a set of numbers S is the smallest non-negative integer that does not occur in the set S.
# In other words, the cost of a partition is the number of segments plus the sum of MEX over all segments.
# Let's define the value of an array b1,b2,…,bk as the maximum possible cost over all partitions of this array.
#
# You are given an array a of size n. Find the sum of values of all its subsegments.
#
# An array x is a subsegment of an array y if x can be obtained from y by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    ans=0
    for i in range(n):
        for j in range(i,n):
            ans+=(j-i+1)+x[i:j+1].count(0)
    print(ans)