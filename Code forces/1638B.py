# You are given an array a1,a2,…,an. You can perform operations on the array.
# In each operation you can choose an integer i (1≤i<n), and swap elements ai and ai+1 of the array, if ai+ai+1 is odd.
#
# Determine whether it can be sorted in non-decreasing order using this operation any number of times.

import sys;input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    even=[i for i in x if(i%2==0)]
    odd=[i for i in x if(i%2==1)]
    print("YES" if (even==sorted(even) and odd==sorted(odd)) else "NO")
