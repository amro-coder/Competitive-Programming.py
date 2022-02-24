# Danik urgently needs rock and lever! Obviously, the easiest way to get these things is to ask Hermit Lizard for them.
# Hermit Lizard agreed to give Danik the lever.
#  But to get a stone, Danik needs to solve the following task.
# You are given a positive integer n, and an array a of positive integers.
#  The task is to calculate the number of such pairs (i,j) that i<j and ai & aj≥ai⊕aj, where & denotes the bitwise AND operation, and ⊕ denotes the bitwise XOR operation.
# Danik has solved this task.
#  But can you solve it?
#
#
#
#  solution:

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    count=[0]*35
    for i in x:
        count[i.bit_length()]+=1
    ans=0
    for i in count:
        ans+=(i*(i-1))//2
    print(ans)
