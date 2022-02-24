# You have an array a of length n.
# You can exactly once select an integer len between 1 and n−1 inclusively,
# and then sort in non-decreasing order the prefix of the array of length len and the suffix of the array of length n−len independently.
#
# For example, if the array is a=[3,1,4,5,2], and you choose len=2, then after that the array will be equal to [1,3,2,4,5].
#
# Could it be that after performing this operation, the array will not be sorted in non-decreasing order?

for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    print("NO" if x==sorted(x) else "YES")