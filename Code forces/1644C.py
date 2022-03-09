# You are given an array a1,a2,…,an, consisting of n integers. You are also given an integer value x.
#
# Let f(k) be the maximum sum of a contiguous subarray of a after applying the following operation:
# add x to the elements on exactly k distinct positions. An empty subarray should also be considered, it has sum 0.
#
# Note that the subarray doesn't have to include all of the increased elements.
#
# Calculate the maximum value of f(k) for all k from 0 to n independently.

# solution:
import sys,itertools
input = sys.stdin.readline
for _ in range(int(input())):
    n, x = map(int, input().split())
    array = list(map(int, input().split()))
    accumlated=[0]+list(itertools.accumulate(array))
    max_sum_of_length=[float("-inf")]*(n+1)
    max_sum_of_length[0]=0
    for i in range(n):
        for j in range(i+1,n+1):
            max_sum_of_length[j-i]=max(max_sum_of_length[j-i],accumlated[j]-accumlated[i])
    last_value=max(*max_sum_of_length,0)
    for i in range(n+1):
        last_value=max(last_value,max(max(max_sum_of_length[i:])+i*x,0))
        print(last_value,end=' ')
    print()
