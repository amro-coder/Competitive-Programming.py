# You are given a sequence of n non-negative integers a1,a2,…,an.
# Initially, all the elements of the sequence are unpainted.
# You can paint each number Red––––– or Blue¯¯¯¯¯¯¯¯¯¯¯ (but not both), or leave it unpainted.
#
# For a color c, Count(c) is the number of elements in the sequence painted with that color and Sum(c) is the sum of the elements in the sequence painted with that color.
#
# For example, if the given sequence is [2,8,6,3,1] and it is painted this way: [2¯¯¯,8,6––,3¯¯¯,1] (where 6 is painted red, 2 and 3 are painted blue, 1 and 8 are unpainted) then Sum(Red–––––)=6, Sum(Blue¯¯¯¯¯¯¯¯¯¯¯)=2+3=5, Count(Red–––––)=1, and Count(Blue¯¯¯¯¯¯¯¯¯¯¯)=2.
#
# Determine if it is possible to paint the sequence so that Sum(Red–––––)>Sum(Blue¯¯¯¯¯¯¯¯¯¯¯) and Count(Red–––––)<Count(Blue¯¯¯¯¯¯¯¯¯¯¯).

import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    x.sort(reverse=True)
    red=0
    count_red=0
    blue=0
    count_blue=0
    i=0
    j=n-1
    while(True):
        if(red>blue and count_red<count_blue):
            print("YES")
            break
        if(i>j):
            print("NO")
            break
        if red<=blue:
            red+=x[i]
            count_red+=1
            i+=1
        else:
            blue+=x[j]
            count_blue+=1
            j-=1