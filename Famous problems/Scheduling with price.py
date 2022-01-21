# problem
# you have n schedule .
# each schedule have a starting time and duration and a value
# you can not pick two schedules that intersect
# note if s1 starts at 10 and have a duration of 10
# and s2 starts at 20
# s1 and s2 can not be picked together
# your task is to find a valid sequence of schedules that maximize the total value

# Solution
# O(n^2) naive implemntation
# import sys
# input=sys.stdin.readline
# for _ in range(int(input())):
#     n=int(input())
#     x=[]
#     for __ in range(n):
#         x.append(tuple(map(int,input().split())))
#     x.sort()
#     dp=[x[i][2] for i in range(n)]
#     dp[-1]=x[-1][-1]
#     for i in range(n-2,-1,-1):
#         for j in range(i+1,n):
#             if(x[j][0]>x[i][0]+x[i][1]):
#                 dp[i] = max(dp[i], x[i][2] + dp[j])
#     print(max(dp))
# O(nlog(n)) solution
import sys
input=sys.stdin.readline
def binSearch(low,high,target):
    while(low<=high):
        mid=(low+high)//2
        if(x[mid][0]>target):
            high=mid-1
        else:
            low=mid+1
    if(low>=n):
        return -1
    return low
for _ in range(int(input())):
    n=int(input())
    x=[]
    for __ in range(n):
        x.append(tuple(map(int,input().split())))
    x.sort()
    dp=[0]*n
    dp[-1]=x[-1][-1]
    for i in range(n-2,-1,-1):
        temp=binSearch(i,n-1,x[i][0]+x[i][1])
        if(temp==-1):
            temp=0
        else:
            temp=dp[temp]
        dp[i]=max(dp[i+1],x[i][2]+temp)
    print(dp[0])

