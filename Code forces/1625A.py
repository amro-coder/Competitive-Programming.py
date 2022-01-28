# Martian scientists explore Ganymede, one of Jupiter's numerous moons. Recently, they have found ruins of an ancient civilization.
# The scientists brought to Mars some tablets with writings in a language unknown to science.
#
# They found out that the inhabitants of Ganymede used an alphabet consisting of two letters, and each word was exactly ℓ letters long.
# So, the scientists decided to write each word of this language as an integer from 0 to 2ℓ−1 inclusively.
# The first letter of the alphabet corresponds to zero bit in this integer, and the second letter corresponds to one bit.
#
# The same word may have various forms in this language. Then, you need to restore the initial form.
# The process of doing it is described below.
#
# Denote the distance between two words as the amount of positions, in which these words differ.
# For example, the distance between 10012 and 11002 (in binary) is equal to two, as these words have different letters in the second and the fourth positions, counting from left to right.
# Further, denote the distance between words x and y as d(x,y).
#
# Let the word have n forms, the i-th of which is described with an integer xi.
# All the xi are not necessarily different, as two various forms of the word can be written the same.
# Consider some word y. Then, closeness of the word y is equal to the sum of distances to each of the word forms, i. e. the sum d(xi,y) over all 1≤i≤n.
# The initial form is the word y with minimal possible nearness.
# You need to help the scientists and write the program which finds the initial form of the word given all its known forms.
# Note that the initial form is not necessarily equal to any of the n given forms.

# solution:
import sys

input = sys.stdin.readline


def closness(x, y):
    x = list(bin(x))[2:]
    if (len(y) > len(x)):
        x = (['0'] * (len(y) - len(x))) + x
    ans = 0
    for i in range(len(x)):
        if (x[i] != y[i]):
            ans += 1
    return ans


for _ in range(int(input())):
    n, l = map(int, input().split())
    x = tuple(map(int, input().split()))
    y = ['0'] * l
    for i in range(l):
        bef = 0
        for j in x:
            bef += closness(j, y)
        y[i] = '1'
        aft = 0
        for j in x:
            aft += closness(j, y)
        if (bef < aft):
            y[i] = '0'
    ans = 0
    for i in range(len(y) - 1, -1, -1):
        ans += (2 ** (len(y) - 1 - i)) * int(y[i])
    print(ans)
