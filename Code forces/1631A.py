# You are given two arrays a and b of n positive integers each.
# You can apply the following operation to them any number of times:
#
# Select an index i (1≤i≤n) and swap ai with bi (i. e. ai becomes bi and vice versa).
# Find the minimum possible value of max(a1,a2,…,an)⋅max(b1,b2,…,bn) you can get after applying such operation any number of times (possibly zero).

# solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(n):
        if(a[i]>b[i]):
            a[i],b[i]=b[i],a[i]
    print(max(a)*max(b))