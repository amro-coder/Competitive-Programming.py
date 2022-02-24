# You are given the array a consisting of n positive (greater than zero) integers.
# In one move, you can choose two indices i and j (i≠j) such that the absolute difference between ai and aj is no more than one (|ai−aj|≤1) and remove the smallest of these two elements.
#  If two elements are equal, you can remove any of them (but exactly one).
# Your task is to find if it is possible to obtain the array consisting of only one element using several (possibly, zero) such moves or not.
# You have to answer t independent test cases.
#
#
#
#  solution:

for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    x.sort()
    for i in range(len(x)-1):
        if(x[i+1]-x[i]>1):
            print("NO")
            break
    else:
        print("YES")