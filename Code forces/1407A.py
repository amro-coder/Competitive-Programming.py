# Alexandra has an even-length array a, consisting of 0s and 1s.
# The elements of the array are enumerated from 1 to n.
# She wants to remove at most n2 elements (where n — length of array) in the way that alternating sum of the array will be equal 0 (i.e. a1−a2+a3−a4+…=0).
# In other words, Alexandra wants sum of all elements at the odd positions and sum of all elements at the even positions to become equal.
# The elements that you remove don't have to be consecutive.
#
# For example, if she has a=[1,0,1,0,0,0] and she removes 2nd and 4th elements, a will become equal [1,1,0,0] and its alternating sum is 1−1+0−0=0.
#
# Help her!

# solution:
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    ones=x.count(1)
    if(ones>n-ones):
        size=ones&((1<<11)-2)
        print(size)
        print(*[1 for _ in range(size)])
    else:
        print(n-ones)
        print(*[0 for __ in range(n-ones)])