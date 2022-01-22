#problem statement:
# You are given a string s, consisting of lowercase Latin letters. Every letter appears in it no more than twice.
# Your task is to rearrange the letters in the string in such a way that for each pair of letters that appear exactly twice, the distance between the letters in the pair is the same.
# You are not allowed to add or remove letters.
# It can be shown that the answer always exists. If there are multiple answers, print any of them.

#solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    string=list(input().strip())
    string.sort()
    print(''.join(string))