# Let's call a permutation p of length n anti-Fibonacci if the condition pi−2+pi−1≠pi holds for all i (3≤i≤n).
# Recall that the permutation is the array of length n which contains each integer from 1 to n exactly once.
#
# Your task is for a given number n print n distinct anti-Fibonacci permutations of length n.

# solution:
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    if(n%2==0):
        for i in range(n):
            ans = [i for i in range(n, 0, -1)]
            ans[0],ans[i]=ans[i],ans[0]
            print(*ans)
    else:
        for i in range(n):
            ans = [i for i in range(n, 0, -1)]
            ans[1],ans[i]=ans[i],ans[1]
            print(*ans)
