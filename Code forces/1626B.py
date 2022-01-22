#problem statement
# You are given a decimal representation of an integer x without leading zeros.
# You have to perform the following reduction on it exactly once:
# take two neighboring digits in x and replace them with their sum without leading zeros (if the sum is 0, it's represented as a single 0).
#
# For example, if x=10057, the possible reductions are:
#
# choose the first and the second digits 1 and 0, replace them with 1+0=1; the result is 1057;
# choose the second and the third digits 0 and 0, replace them with 0+0=0; the result is also 1057;
# choose the third and the fourth digits 0 and 5, replace them with 0+5=5; the result is still 1057;
# choose the fourth and the fifth digits 5 and 7, replace them with 5+7=12; the result is 10012.
# What's the largest number that can be obtained?

#solution:
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    string = list(input().strip())
    ans = -1
    index = -1
    index2 = len(string) - 2
    for i in range(len(string) - 1):
        temp = str(int(string[i]) + int(string[i + 1]))
        if (len(temp) == 2):
            index = i
        elif (int(temp) > int(string[i])):
            if (index2 == len(string) - 2):
                index2 = i

    if (index != -1):
        string[index:index + 2] = str(int(string[index]) + int(string[index + 1]))
    else:
        string[index2:index2 + 2] = str(int(string[index2]) + int(string[index2 + 1]))
    print(''.join(string))