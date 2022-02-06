#problem:
# Consider the array a composed of all the integers in the range [l,r]. For example, if l=3 and r=7, then a=[3,4,5,6,7].
#
# Given l, r, and k, is it possible for gcd(a) to be greater than 1 after doing the following operation at most k times?
#
# Choose 2 numbers from a.
# Permanently remove one occurrence of each of them from the array.
# Insert their product back into a.
# gcd(b) denotes the greatest common divisor (GCD) of the integers in b.

#solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    l,r,k=map(int,input().split())
    if(l==r):
        if(l>1):
            print("YES")
        else:
            print("NO")
        continue
    numberOfOdds=((r+1)//2)-(l//2)
    if(k>=numberOfOdds):
        print("YES")
    else:
        print("NO")