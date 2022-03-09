# Luis has a sequence of n+1 integers a1,a2,…,an+1. For each i=1,2,…,n+1 it is guaranteed that 0≤ai<n, or ai=n2.
# He has calculated the sum of all the elements of the sequence, and called this value s.
#
# Luis has lost his sequence, but he remembers the values of n and s.
# Can you find the number of elements in the sequence that are equal to n2?
#
# We can show that the answer is unique under the given constraints.

# solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,s=map(int,input().split())
    print(s//(n**2))
