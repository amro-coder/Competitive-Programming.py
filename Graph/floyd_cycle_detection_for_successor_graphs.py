n= int(input())
# n+=1 # if the first node is one
successor=[-1]*n
# each node must have exactly one child, in other words the out degree of each node is 1
for _ in range(n):
    a, b = map(int, input().split())
    successor[a]=b
x=0
# we increase one pointer by one and the other pointer by two the have to meet in the cycle
a=successor[x]
b=successor[successor[x]]
while a!=b:
    a=successor[a]
    b = successor[successor[b]]
# let's assume they met after k moves then the length of the cycle is divisble by k
# and to find the start of the cycle we start two pointers from x and the point they met and increase each of them, they will meat in the start of the cycle
b=x
while a!=b:
    a = successor[a]
    b = successor[b]
cycle_start=a
# now all is left is to calculate the length of the cycle
a=successor[a]
length=1
while a!=cycle_start:
    a=successor[a]
    length+=1

print(f"the cycle starts at node {cycle_start} and cycle length = {length}")

# 7
# 0 1
# 1 2
# 2 5
# 5 6
# 6 3
# 3 5
# 4 5

