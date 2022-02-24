# You are given an array a, consisting of n integers.
#
# Each position i (1≤i≤n) of the array is either locked or unlocked.
# You can take the values on the unlocked positions, rearrange them in any order and place them back into the unlocked positions.
# You are not allowed to remove any values, add the new ones or rearrange the values on the locked positions.
# You are allowed to leave the values in the same order as they were.
#
# For example, let a=[−1,1,3–,2,−2–––,1,−4,0–], the underlined positions are locked. You can obtain the following arrays:
#
# [−1,1,3–,2,−2–––,1,−4,0–];
# [−4,−1,3–,2,−2–––,1,1,0–];
# [1,−1,3–,2,−2–––,1,−4,0–];
# [1,2,3–,−1,−2–––,−4,1,0–];
# and some others.
# Let p be a sequence of prefix sums of the array a after the rearrangement. So p1=a1, p2=a1+a2, p3=a1+a2+a3, …, pn=a1+a2+⋯+an.
#
# Let k be the maximum j (1≤j≤n) such that pj<0. If there are no j such that pj<0, then k=0.
#
# Your goal is to rearrange the values in such a way that k is minimum possible.
#
# Output the array a after the rearrangement such that the value k for it is minimum possible.
# If there are multiple answers then print any of them.

# solution:

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    locked=list(map(int,input().split()))
    order=sorted([x[i] for i in range(n) if(not locked[i])],reverse=True)
    ans=[]
    j=0
    for i in range(n):
        if(locked[i]):
            ans.append(x[i])
        else:
            ans.append(order[j])
            j+=1
    print(*ans)