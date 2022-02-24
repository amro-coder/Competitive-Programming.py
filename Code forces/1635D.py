# You are given an array a consisting of n distinct positive integers.
# x=ai for some 1≤i≤n.
# x=2y+1 and y is in S.
# x=4y and y is in S.
# For example, if a=[1,2] then the 10 smallest elements in S will be {1,2,3,4,5,7,8,9,11,12}.
# Find the number of elements in S that are strictly smaller than 2p.
#  Since this number may be too large, print it modulo 109+7.
#
#
#
#  solution:

import sys,math
input = sys.stdin.readline
mod=10**9+7
n,p=map(int,input().split())
x=list(sorted(map(int,input().split())))
def parnet_exist(x):
    while (x):
        if (x in useful_elements):
            return True
        if (x & 1):
            x >>= 1
        else:
            if (x & 3):#can not be divided by 4
                return False
            x >>= 2
    return False
useful_elements=set()
for i in x:
    if(not parnet_exist(i)):
        useful_elements.add(i)
dp=[0]*(3*10**5)
for i in useful_elements:
    dp[math.floor(math.log(i,2))]+=1
for i in range(p):
    dp[i]+=(dp[i-1]+dp[i-2])%mod
print(sum(dp[:p])%mod)
