# You are given an array a of n elements.
# Your can perform the following operation no more than n times: Select three indices x,y,z (1≤x<y<z≤n) and replace ax with ay−az.
#  After the operation, |ax| need to be less than 1018.
# Your goal is to make the resulting array non-decreasing.
#  If there are multiple solutions, you can output any.
#  If it is impossible to achieve, you should report it as well.
#
#
#
#  solution:

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    if(x[-2]>x[-1]):
        print(-1)
    else:
        if(x[-2]-x[-1]>x[-2]):
            if(list(sorted(x))==x):
                print(0)
            else:
                print(-1)
        else:
            print(n - 2)
            for i in range(1, n - 1):
                print(i, n - 1, n)

