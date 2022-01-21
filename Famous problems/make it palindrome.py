# problem statement:
# A palindrome is a string that reads the same forward and backward
# you are a given a string s
# make the string palindrome with minimum number of insertions
# you can insert in any position

# solution
import sys
input=sys.stdin.readline
string = list(input().strip())
n = len(string)
dp = [[0] * n for _ in range(n)]
for diff in range(1, n):
    for j in range(n - diff):
        if (string[j] == string[j + diff]):
            dp[j][j + diff] = dp[j + 1][j + diff - 1]
        else:
            dp[j][j + diff] = min(dp[j][j + diff - 1], dp[j + 1][j + diff]) + 1
print(dp[0][-1])