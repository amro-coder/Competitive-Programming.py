# You are given an array a of n positive integers numbered from 1 to n.
# Let's call an array integral if for any two, not necessarily different, numbers x and y from this array, x≥y, the number ⌊xy⌋ (x divided by y with rounding down) is also in this array.
#
# You are guaranteed that all numbers in a do not exceed c.
# Your task is to check whether this array is integral.

import sys
input= sys.stdin.readline

for _ in range(int(input())):
    n,c=map(int,input().split())
    x=list(set(map(int,input().split())))
    n=len(x)
    x.sort()
    max_x=x[-1]
    if x[0]!=1:
        print("No")
        continue

    count=[0]*(max_x+1)
    for i in x:
        count[i]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]

    r_candiates=[]
    index=0
    for i in range(1,max_x+1):
        if(index==n):
            break
        if i!=x[index]:
            r_candiates.append(i)
        else:
            index+=1

    ans=True
    for i in r_candiates:
        for j in range(1,n):
            if i*x[j]>max_x:
                break
            if count[min(len(count)-1,x[j]*(i+1)-1)]-count[i*x[j]-1]:
                ans=False
                break
    print("Yes" if ans else "No")


