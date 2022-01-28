# This problem's actual name, "Lexicographically Largest Palindromic Subsequence" is too long to fit into the page headline.
#
# You are given string s consisting of lowercase English letters only. Find its lexicographically largest palindromic subsequence.
# String x = x1x2... x|x| is lexicographically larger than string y = y1y2... y|y| if either |x| > |y| and x1 = y1, x2 = y2, ..., x|y| = y|y|, or there exists such number r (r < |x|, r < |y|) that x1 = y1, x2 = y2, ..., xr = yr and xr  +  1 > yr  +  1. Characters in the strings are compared according to their ASCII codes.
# For example, string "ranger" is lexicographically larger than string "racecar" and string "poster" is lexicographically larger than string "post".
# String s = s1s2... s|s| is a palindrome if it matches string rev(s) = s|s|s|s| - 1... s1. In other words, a string is a palindrome if it reads the same way from left to right and from right to left.
# For example, palindromic strings are "racecar", "refer" and "z".

#solution:
s=list(input())
print(max(s)*s.count(max(s)))