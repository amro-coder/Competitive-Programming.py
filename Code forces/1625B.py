# Martians are actively engaged in interplanetary trade.
# Olymp City, the Martian city known for its spaceport, has become a place where goods from all the corners of our Galaxy come.
# To deliver even more freight from faraway planets, Martians need fast spaceships.
#
# A group of scientists conducts experiments to build a fast engine for the new spaceship.
# In the current experiment, there are n elementary particles, the i-th of them has type ai.
#
# Denote a subsegment of the particle sequence (a1,a2,…,an) as a sequence (al,al+1,…,ar) for some left bound l and right bound r (1≤l≤r≤n).
# For instance, the sequence (1 4 2 8 5 7) for l=2 and r=4 has the sequence (4 2 8) as a subsegment.
# Two subsegments are considered different if at least one bound of those subsegments differs.
#
# Note that the subsegments can be equal as sequences but still considered different.
# For example, consider the sequence (1 1 1 1 1) and two of its subsegments: one with l=1 and r=3 and another with l=2 and r=4.
# Both subsegments are equal to (1 1 1), but still considered different, as their left and right bounds differ.
#
# The scientists want to conduct a reaction to get two different subsegments of the same length. Denote this length k.
# The resulting pair of subsegments must be harmonious, i. e.
# for some i (1≤i≤k) it must be true that the types of particles on the i-th position are the same for these two subsegments.
# For example, the pair (1 7 3) and (4 7 8) is harmonious, as both subsegments have 7 on the second position.
# The pair (1 2 3) and (3 1 2) is not harmonious.
#
# The longer are harmonious subsegments, the more chances for the scientists to design a fast engine.
# So, they asked you to calculate the maximal possible length of harmonious pair made of different subsegments.


import sys
from collections import defaultdict
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = tuple(map(int, input().split()))
    ans = -1
    min2 = defaultdict(list)
    for i in range(n):
        min2[x[i]].append(i)
    for key, value in min2.items():
        bestDiff = float('inf')
        for i in range(len(value) - 1):
            bestDiff=min(value[i+1]-value[i],bestDiff)
        min2[key] = bestDiff
    for key, value in min2.items():
        if (value != float('inf')):
            ans = max(ans, n -value)
    print(ans)