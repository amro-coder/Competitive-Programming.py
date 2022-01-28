# Alice gave Bob two integers a and b (a>0 and b≥0).
# Being a curious boy, Bob wrote down an array of non-negative integers with MEX value of all elements equal to a and XOR value of all elements equal to b.
#
# What is the shortest possible length of the array Bob wrote?
#
# Recall that the MEX (Minimum EXcluded) of an array is the minimum non-negative integer that does not belong to the array and the XOR of an array is the bitwise XOR of all the elements of the array.

#solution:
for _ in range(int(input())):
    mex,xor=map(int,input().split())
    n =mex-1
    temp = n % 4
    if (temp == 0):
        ans=n
    elif (temp == 1):
        ans=1
    elif (temp == 2):
        ans=n+1
    else:
        ans=0
    if(ans==xor):
        print(mex)
    else:
        if(ans^xor!=mex):
            print(mex+1)
        else:
            print(mex+2)
