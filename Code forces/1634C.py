# You work for a well-known department store that uses leading technologies and employs mechanistic work — that is, robots!
#
# The department you work in sells n⋅k items. The first item costs 1 dollar,
# the second item costs 2 dollars, and so on: i-th item costs i dollars. The items are situated on shelves.
# The items form a rectangular grid: there are n shelves in total, and each shelf contains exactly k items.
# We will denote by ai,j the price of j-th item (counting from the left) on the i-th shelf, 1≤i≤n,1≤j≤k.
#
# Occasionally robots get curious and ponder on the following question:
# what is the mean price (arithmetic average) of items ai,l,ai,l+1,…,ai,r for some shelf i and indices l≤r? Unfortunately,
# the old robots can only work with whole numbers.
# If the mean price turns out not to be an integer, they break down.
#
# You care about robots' welfare. You want to arrange the items in such a way that the robots cannot theoretically break.
# Formally, you want to choose such a two-dimensional array a that:
#
# Every number from 1 to n⋅k (inclusively) occurs exactly once.
# For each i,l,r, the mean price of items from l to r on i-th shelf is an integer.
# Find out if such an arrangement is possible, and if it is, give any example of such arrangement.

import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    odd = ((n * k) + 1) // 2
    even = (n * k) - odd
    if (even % k == 0 and odd % k == 0):
        print("YES")
        last = 1
        for _ in range(odd // k):
            for __ in range(k):
                print(last, end=' ')
                last += 2
            print()
        last = 2
        for _ in range(even // k):
            for __ in range(k):
                print(last, end=' ')
                last += 2
            print()

    else:
        print("NO")