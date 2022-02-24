# You are given an array a of size n.
# Choose two different integers i,j (1≤i<j≤n), replace ai with x and aj with y.
#  In order not to break the array, ai|aj=x|y must be held, where | denotes the bitwise OR operation.
#  Notice that x and y are non-negative integers.
# Please output the minimum sum of the array you can get after using the operation above any number of times.
#
#
#
#  solution:

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    ans=0
    for i in x:
        ans|=i
    print(ans)