# problem:
# Mihai has just learned about the MEX concept and since he liked it so much, he decided to use it right away.
#
# Given an array a of n non-negative integers, Mihai wants to create a new array b that is formed in the following way:
#
# While a is not empty:
#
# Choose an integer k (1≤k≤|a|).
# Append the MEX of the first k numbers of the array a to the end of array b and erase them from the array a, shifting the positions of the remaining numbers in a.
# But, since Mihai loves big arrays as much as the MEX concept, he wants the new array b to be the lexicographically maximum.
# So, Mihai asks you to tell him what the maximum array b that can be created by constructing the array optimally is.
#
# An array x is lexicographically greater than an array y
# if in the first position where x and y differ xi>yi or if |x|>|y| and y is a prefix of x (where |x| denotes the size of the array x).
# The MEX of a set of non-negative integers is the minimal non-negative integer such that it is not in the set.
# For example, MEX({1,2,3}) =0 and MEX({0,1,2,4,5}) =3.
#
# solution:
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = tuple(map(int, input().split()))
    count = [[] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        count[x[i]].append(i)
    minimum = -1
    lastIndex = -1
    check = False
    ans = []
    key = 0
    while (True):
        if (count[key]):
            temp = count[key].pop()
            if (temp > minimum):
                check = True
                lastIndex = max(lastIndex, temp)
                key += 1
        else:
            if (not check):
                lastIndex += 1
            minimum = lastIndex
            ans.append(key)
            check = False
            key = 0
            if (lastIndex == n - 1):
                break

    print(len(ans))
    print(*ans)