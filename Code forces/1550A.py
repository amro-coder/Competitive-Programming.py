# Let's call an array a consisting of n positive (greater than 0) integers beautiful if the following condition is held for every i from 1 to n: either ai=1, or at least one of the numbers ai−1 and ai−2 exists in the array as well.
#
# For example:
#
# the array [5,3,1] is beautiful: for a1, the number a1−2=3 exists in the array; for a2, the number a2−2=1 exists in the array; for a3, the condition a3=1 holds;
# the array [1,2,2,2,2] is beautiful: for a1, the condition a1=1 holds; for every other number ai, the number ai−1=1 exists in the array;
# the array [1,4] is not beautiful: for a2, neither a2−2=2 nor a2−1=3 exists in the array, and a2≠1;
# the array [2] is not beautiful: for a1, neither a1−1=1 nor a1−2=0 exists in the array, and a1≠1;
# the array [2,1,3] is beautiful: for a1, the number a1−1=1 exists in the array; for a2, the condition a2=1 holds; for a3, the number a3−2=1 exists in the array.
# You are given a positive integer s. Find the minimum possible size of a beautiful array with the sum of elements equal to s.

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    total=0
    ans=0
    i=1
    while(total<n):
        ans+=1
        total+=i
        i+=2
        if(total>=n):
            break
    print(ans)