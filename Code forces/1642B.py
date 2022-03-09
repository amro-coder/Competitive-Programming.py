# Sam is a kindergartener, and there are n children in his group.
#  He decided to create a team with some of his children to play "brawl:go 2".
# Sam has n power-ups, the i-th has type ai.
#  A child's strength is equal to the number of different types among power-ups he has.
# For a team of size k, Sam will distribute all n power-ups to k children in such a way that each of the k children receives at least one power-up, and each power-up is given to someone.
# For each integer k from 1 to n, find the minimum sum of strengths of a team of k children Sam can get.
#
#
#
#  solution:

import sys
from collections import Counter
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    count=dict(Counter(x))
    for i in range(1,n+1):
        print(max(i,len(count)),end=' ')
    print()
