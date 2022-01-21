# Problem Statement:
# It's dinner time in Castle Camelot, and the fearsome Knights of the Round Table are clamouring for dessert.
# You, the chef, are in a soup. There are N knights, including King Arthur, each with a different preference for dessert, but you cannot afford to make desserts for all of them.
# You are given the cost of manufacturing each Knight's preferred dessert–since it is a round table, the list starts with the cost of King Arthur's dessert, and goes counter-clockwise.
# You decide to pick the cheapest desserts to make, such that for every pair of adjacent Knights, at least one gets his dessert.
# This will ensure that the Knights do not protest.
# What is the minimum cost of tonight's dinner, given this condition?
# For instance, suppose there are 5 Knights and their desserts cost 1, 2, 1, 2 and 2.
# In this case, the minimum cost is 4, which you can achieve by feeding the first, third and fourth (or fifth) Knights.
#
# Input format
# There are 2 lines of input.
# The first line contains a single integer N, the number of seats at the table.
# The next line contains N space separated integers, each being the cost of the dessert of a Knight, listed in counterclockwise order around the table, starting with King Arthur.
#
# Output format
# The output should be a single line containing a single integer, the minimum possible cost for you, the chef.
#
#
# Solution:
import sys
input=sys.stdin.readline
n=int(input())
x=list(map(int,input().split()))
if(n<=2):
    print(min(x))
    exit()
# including first element
dp1=[0]*n
dp1[-1]=x[-1]
dp1[-2]=x[-2]
for i in range(n-3,-1,-1):
    dp1[i]=x[i]+min(dp1[i+2],dp1[i+1])

x.reverse()
# including last element
dp2=[0]*n
dp2[-1]=x[-1]
dp2[-2]=x[-2]
for i in range(n-3,-1,-1):
    dp2[i]=x[i]+min(dp2[i+2],dp2[i+1])
print(min(dp1[0],dp2[0]))




