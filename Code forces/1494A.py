# You are given a string a, consisting of n characters, n is even.
# For each i from 1 to n ai is one of 'A', 'B' or 'C'.
#
# A bracket sequence is a string containing only characters "(" and ")".
# A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting characters "1" and "+" between the original characters of the sequence.
# For example, bracket sequences "()()" and "(())" are regular (the resulting expressions are: "(1)+(1)" and "((1+1)+1)"), and ")(", "(" and ")" are not.
#
# You want to find a string b that consists of n characters such that:
#
# b is a regular bracket sequence;
# if for some i and j (1≤i,j≤n) ai=aj, then bi=bj.
# In other words, you want to replace all occurrences of 'A' with the same type of bracket, then all occurrences of 'B' with the same type of bracket and all occurrences of 'C' with the same type of bracket.
#
# Your task is to determine if such a string b exists.

#solution:
for _ in range(int(input())):
    x = tuple(input().strip())
    chars = {}
    for i in x:
        chars[i] = 0
    keys = list(chars.keys())
    if (len(keys) == 1):
        print("NO")
    else:
        start = keys[0]
        end = x[-1]
        open = 0
        ans = True
        for i in x:
            if (i != start):
                open -= 1
            else:
                open += 1
            if (open < 0):
                ans = False
                break
        if (open > 0):
            ans = False

        open = 0
        ans2 = True
        for i in x:
            if (i != end):
                open += 1
            else:
                open -= 1
            if (open < 0):
                ans2 = False
                break
        if (open > 0):
            ans2 = False

        if (ans2 or ans):
            print("YES")
        else:
            print("NO")
