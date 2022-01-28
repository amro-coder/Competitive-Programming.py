# Given an integer n, find the maximum value of integer k such that the following condition holds:
#
# n & (n−1) & (n−2) & (n−3) & ... (k) = 0
# where & denotes the bitwise AND operation.

# solution:
import sys,math
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    print(2**math.floor(math.log(n,2))-1)