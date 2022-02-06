# It has finally been decided to build a roof over the football field in School 179. Its construction will require placing n consecutive vertical pillars. Furthermore, the headmaster wants the heights of all the pillars to form a permutation p of integers from 0 to n−1,
# where pi is the height of the i-th pillar from the left (1≤i≤n).
#
# As the chief, you know that the cost of construction of consecutive pillars is equal to the maximum value of the bitwise XOR of heights of all pairs of adjacent pillars.
# In other words, the cost of construction is equal to max1≤i≤n−1pi⊕pi+1, where ⊕ denotes the bitwise XOR operation.
#
# Find any sequence of pillar heights p of length n with the smallest construction cost.
#
# In this problem, a permutation is an array consisting of n distinct integers from 0 to n−1 in arbitrary order.
# For example, [2,3,1,0,4] is a permutation, but [1,0,1] is not a permutation (1 appears twice in the array) and [1,0,3] is also not a permutation (n=3, but 3 is in the array).

# solution:
import sys,math
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    mid=2**math.floor(math.log(n-1,2))
    ans=[]
    ans.extend([i for i in range(mid,n)])
    start=(n-1)-mid
    ans.extend([i for i in range(start, mid)])
    ans.extend([i for i in range(start)])
    print(*ans)
