# Problem Statement:
# Calvin wakes up early one morning and finds that all his friends in the hostel are asleep.
# To amuse himself, he decides to play the following game : he draws a sequence of N squares on the ground, numbered 1 to N, and writes an integer in each square.
# He starts at square k (1 ≤ k ≤ N). The game consists of one forward phase followed by one backward phase.
# In the forward phase, Calvin makes zero or more moves of the following type :
# if his current position is p, he can jump to p+1 or p+2 as long as he stays within the N squares.
#
# In the backward phase, Calvin makes zero or more moves of the following type :
# if his current position is p, he can jump to p−1 or p−2 as long as he stays within the N squares.
#
# He plays such that he finally ends up at square 1, and then he stops.
# He starts with a score of 0, and each time he jumps from square i to square j, he adds the integer written in square j to his score.
# Find the maximum score Calvin can obtain by playing this game.
# Recall that Calvin must start at square k and end at square 1.
# The integer on the square where he starts is not included in his score.
#
# For example, suppose N = 5 and the numbers in squares are 5, 3, −2, 1, 1. If k = 2 Calvin starts on the second square.
# He can make a forward move to square 4, another to square 5, a backward move to square 4, another to square 2, and another to square 1.
# His total score is 1+1+1+3+5 = 11. You can check that this is the maximum score possible.
#
# Input format
# • Line 1 : Two space-separated integers, N and k, with 1 ≤ k ≤ N.
# • Line 2 : A space-separated sequence of N integers, the numbers in squares 1, 2 . . . , N .
#
# Output format
# A single line with a single integer, the maximum score Calvin can obtain by playing the game.

# Solution
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
x=tuple(map(int,input().split()))
dp=[float('-inf')]*n
dp[0]=0
for i in range(1,n):
    for j in [i-1,i-2]:
        if(j>=0):
            dp[i]=max(dp[i],x[j]+dp[j])
for i in range(n-2,k-2,-1):
    for j in [i+1,i+2]:
        if(j<n):
            dp[i]=max(dp[i],x[j]+dp[j])
print(dp[k-1])