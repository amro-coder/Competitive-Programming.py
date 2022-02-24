# You are given a string s of length n and a number k. Let's denote by rev(s) the reversed string s (i.e. rev(s)=snsn−1...s1).
# You can apply one of the two kinds of operations to the string:
#
# replace the string s with s+rev(s)
# replace the string s with rev(s)+s
# How many different strings can you get as a result of performing exactly k operations (possibly of different kinds) on the original string s?
#
# In this statement we denoted the concatenation of strings s and t as s+t.
# In other words, s+t=s1s2...snt1t2...tm, where n and m are the lengths of strings s and t respectively.

#solution:
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    string = list(input().strip())
    if (string == list(reversed(string)) or k == 0):
        print(1)
    else:
        print(2)