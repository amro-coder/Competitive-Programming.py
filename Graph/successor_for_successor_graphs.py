# we want to find the successor of each node in O(log(n)) after n log(u) preprocessing. u is the largest successor we could ask for.
import math
def xth_successor(node,x):
    n=x.bit_length()-1
    for i in range(n,-1,-1):
        if x>>i&1:
            node=dp_successor[i][node]
    return node

n= int(input())
# n+=1 # if the first node is one
successor=[-1]*n
# each node must have exactly one child, in other words the out degree of each node is 1
for _ in range(n):
    a, b = map(int, input().split())
    successor[a]=b
u=1024 # max number to be asked as a successor
max_power_of_two=math.floor(math.log(u,2))
print(successor)
dp_successor=[[-1]*n for _ in range(max_power_of_two+1)]
# dp_successor[i][j] represents the 2**i successor for the node j
dp_successor[0]=successor.copy()
for i in range(1,max_power_of_two+1):
    for node in range(n):
        dp_successor[i][node]=dp_successor[i-1][dp_successor[i-1][node]]
print(xth_successor(0,1))
print(xth_successor(0,2))
print(xth_successor(0,3))
print(xth_successor(0,4))
print(xth_successor(0,5))
print(xth_successor(0,6))
print(xth_successor(0,7))
print(xth_successor(0,8))
print(xth_successor(0,9))
print(xth_successor(0,10))
print(xth_successor(0,11))
print(xth_successor(0,12))

# 7
# 0 1
# 1 2
# 2 5
# 5 6
# 6 3
# 3 5
# 4 5

