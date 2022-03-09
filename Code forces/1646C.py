# A number is called powerful if it is a power of two or a factorial.
# In other words, the number m is powerful if there exists a non-negative integer d such that m=2d or m=d!, where d!=1⋅2⋅…⋅d (in particular, 0!=1).
# For example 1, 4, and 6 are powerful numbers, because 1=1!, 4=22, and 6=3! but 7, 10, or 18 are not.
#
# You are given a positive integer n.
# Find the minimum number k such that n can be represented as the sum of k distinct powerful numbers, or say that there is no such k.

from itertools import combinations
fact=[0,1]
while(fact[-1]<10**13):
    fact.append(fact[-1]*len(fact))
fact.pop(0)
all_fact_sums=[set() for _ in range(17)]
for i in range(1,17):
    for comb in combinations(fact,i):
        all_fact_sums[i].add(sum(comb))
all_fact_sums[0].add(0)

import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    ans=float("inf")
    for i in range(len(all_fact_sums)):
        for j in all_fact_sums[i]:
            if j<=n:
                ans=min(ans,i+bin(n-j).count("1"))
    print(ans)
