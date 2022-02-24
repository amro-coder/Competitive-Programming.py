# You are given a string s of length n consisting only of the characters 0 and 1.
# You perform the following operation until the string becomes empty: choose some consecutive substring of equal characters, erase it from the string and glue the remaining two parts together (any of them can be empty) in the same order.
#  For example, if you erase the substring 111 from the string 111110, you will get the string 110.
#  When you delete a substring of length l, you get a⋅l+b points.
# Your task is to calculate the maximum number of points that you can score in total, if you have to make the given string empty.
#
#
#
#  solution:


import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    string=tuple(input())
    if(b==0):
        print(n*a)
    elif(b>0):
        print(n*(a+b))
    else:
        zeros=ones=0
        prev=-1
        for i in range(n):
            if(string[i]=="0" and prev!=0):
                zeros+=1
                prev=0
            elif (string[i] == "1" and prev != 1):
                ones +=1
                prev = 1
            else:
                prev=int(string[i])
        print((min(ones,zeros)+1)*(b)+(n*a))
