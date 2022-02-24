# Suppose you have two points p=(xp,yp) and q=(xq,yq).
#  Let's denote the Manhattan distance between them as d(p,q)=|xp−xq|+|yp−yq|.
# Let's say that three points p, q, r form a bad triple if d(p,r)=d(p,q)+d(q,r).
# Let's say that an array b1,b2,…,bm is good if it is impossible to choose three distinct indices i, j, k such that the points (bi,i), (bj,j) and (bk,k) form a bad triple.
# You are given an array a1,a2,…,an.
#  Calculate the number of good subarrays of a.
#  A subarray of the array a is the array al,al+1,…,ar for some 1≤l≤r≤n.
# Note that, according to the definition, subarrays of length 1 and 2 are good.
#
#
#
#  solution:

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=tuple(map(int,input().split()))
    # counting bad sub arrays
    ans=0
    # length 3
    for i in range(n-2):
        if(x[i]<=x[i+1] and x[i+1]<=x[i+2]) or (x[i]>=x[i+1] and x[i+1]>=x[i+2]):
            ans+=1
    # length 4
    for i in range(n - 3):
        if (x[i] <= x[i + 1] and x[i + 1] <= x[i + 2]) or (x[i] >= x[i + 1] and x[i + 1] >= x[i + 2]) or (x[i] <= x[i + 1] and x[i + 1] <= x[i + 3]) or (x[i] >= x[i + 1] and x[i + 1] >= x[i + 3]) or (x[i] <= x[i + 2] and x[i + 2] <= x[i + 3]) or (x[i] >= x[i + 2] and x[i + 2] >= x[i + 3]) or (x[i+1] <= x[i + 2] and x[i + 2] <= x[i + 3]) or (x[i+1] >= x[i + 2] and x[i + 2] >= x[i + 3]):
            ans += 1
    if(n>=4):
        print((4 * n - 6) - ans)
    elif(n==3):
        print((3 * n - 3) - ans)
    elif(n==2):
        print((2 * n - 1) - ans)
    else:
        print(n-ans)