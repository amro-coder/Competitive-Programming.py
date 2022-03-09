# A sequence of positive integers is called great for a positive integer x, if we can split it into pairs in such a way that in each pair the first number multiplied by x is equal to the second number.
#  More formally, a sequence a of size n is great for a positive integer x, if n is even and there exists a permutation p of size n, such that for each i (1≤i≤n2) ap2i−1⋅x=ap2i.
# Sam has a sequence a and a positive integer x.
#  Help him to make the sequence great: find the minimum possible number of positive integers that should be added to the sequence a to make it great for the number x.
#
#
#
#  solution:

import sys
from collections import Counter
input = sys.stdin.readline
for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    count=Counter(a)
    ans=0
    for i in a:
        if(count[i]>0):
            if(count[i*x]>0):
                count[i*x]-=1
            else:
                ans+=1
            count[i] -= 1
    print(ans)


