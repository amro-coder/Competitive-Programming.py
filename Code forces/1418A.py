# You are playing a very popular game called Cubecraft.
#  Initially, you have one stick and want to craft k torches.
#  One torch can be crafted using one stick and one coal.
# exchange 1 stick for x sticks (you lose 1 stick and gain x sticks).
# exchange y sticks for 1 coal (you lose y sticks and gain 1 coal).
# During one trade, you can use only one of these two trade offers.
#  You can use each trade offer any number of times you want to, in any order.
# Your task is to find the minimum number of trades you need to craft at least k torches.
#  The answer always exists under the given constraints.
# You have to answer t independent test cases.
#
#
#
#  solution:

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x,y,k=map(int,input().split())
    print(k-(-(k*y+k-1)//(x-1)))
