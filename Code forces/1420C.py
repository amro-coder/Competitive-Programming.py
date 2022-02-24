# This is the easy version of the problem.
#  The difference between the versions is that the easy version has no swap operations.
#  You can make hacks only if all versions of the problem are solved.
# Pikachu is a cute and friendly pokémon living in the wild pikachu herd.
# But it has become known recently that infamous team R wanted to steal all these pokémon! Pokémon trainer Andrew decided to help Pikachu to build a pokémon army to resist.
# First, Andrew counted all the pokémon — there were exactly n pikachu.
#  The strength of the i-th pokémon is equal to ai, and all these numbers are distinct.
# As an army, Andrew can choose any non-empty subsequence of pokemons.
#  In other words, Andrew chooses some array b from k indices such that 1≤b1<b2<⋯<bk≤n, and his army will consist of pokémons with forces ab1,ab2,…,abk.
# The strength of the army is equal to the alternating sum of elements of the subsequence; that is, ab1−ab2+ab3−ab4+….
# Andrew is experimenting with pokémon order.
#  He performs q operations.
#  In i-th operation Andrew swaps li-th and ri-th pokémon.
# Note: q=0 in this version of the task.
# Andrew wants to know the maximal stregth of the army he can achieve with the initial pokémon placement.
#  He also needs to know the maximal strength after each operation.
#
#
#
#  solution:

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,q=map(int,input().split())
    x=list(map(int,input().split()))
    dp=[(0,0)]*n
    dp[-1]=(x[-1],-x[-1])
    for i in range(n-2,-1,-1):
        dp[i]=(max(x[i],x[i]+dp[i+1][1],dp[i+1][0]),max(-x[i],-x[i]+dp[i+1][0],dp[i+1][1]))
    print(max(dp[0]))

