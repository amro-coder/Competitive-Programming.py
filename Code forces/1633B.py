# You are given a string s, consisting only of characters '0' and '1'.
#
# You have to choose a contiguous substring of s and remove all occurrences of the character, which is a strict minority in it, from the substring.
#
# That is, if the amount of '0's in the substring is strictly smaller than the amount of '1's, remove all occurrences of '0' from the substring.
# If the amount of '1's is strictly smaller than the amount of '0's, remove all occurrences of '1'.
# If the amounts are the same, do nothing.
#
# You have to apply the operation exactly once. What is the maximum amount of characters that can be removed?

#solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    string=tuple(input().strip())
    n=len(string)
    ones=0
    for i in string:
        if(i=='1'):
            ones+=1
    if (ones == n - ones):
        print(ones - 1)
    else:
        print(min(ones, n - ones))