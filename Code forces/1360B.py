# There are n athletes in front of you.
#  Athletes are numbered from 1 to n from left to right.
#  You know the strength of each athlete — the athlete number i has the strength si.
# You want to split all athletes into two teams.
#  Each team must have at least one athlete, and each athlete must be exactly in one team.
# You want the strongest athlete from the first team to differ as little as possible from the weakest athlete from the second team.
#  Formally, you want to split the athletes into two teams A and B so that the value |max(A)−min(B)| is as small as possible, where max(A) is the maximum strength of an athlete from team A, and min(B) is the minimum strength of an athlete from team B.
# For example, if n=5 and the strength of the athletes is s=[3,1,2,6,4], then one of the possible split into teams is:
#
# first team: A=[1,2,4],
# second team: B=[3,6].
# In this case, the value |max(A)−min(B)| will be equal to |4−3|=1.
#  This example illustrates one of the ways of optimal split into two teams.
# Print the minimum value |max(A)−min(B)|.
#
#
#
#  solution:

for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    x.sort()
    diff=x[-1]
    for i in range(n-1):
        diff=min(diff,x[i+1]-x[i])
    print(diff)