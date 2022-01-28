# Mocha is a young girl from high school.
# She has learned so much interesting knowledge from her teachers, especially her math teacher.
# Recently, Mocha is learning about binary system and very interested in bitwise operation.
#
# This day, Mocha got a sequence a of length n.
# In each operation, she can select an arbitrary interval [l,r] and for all values i (0≤i≤r−l), replace al+i with al+i&ar−i at the same time, where & denotes the bitwise AND operation.
# This operation can be performed any number of times.
#
# For example, if n=5, the array is [a1,a2,a3,a4,a5], and Mocha selects the interval [2,5], then the new array is [a1,a2&a5,a3&a4,a4&a3,a5&a2].
#
# Now Mocha wants to minimize the maximum value in the sequence. As her best friend, can you help her to get the answer?

#solution:
for _ in range(int(input())):
    n=int(input())
    x=tuple(map(int,input().split()))
    ans=x[0]
    for i in range(n):
        ans=ans&x[i]
    print(ans)