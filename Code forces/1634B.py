# Your friends Alice and Bob practice fortune telling.
#
# Fortune telling is performed as follows. There is a well-known array a of n non-negative integers indexed from 1 to n.
# The tellee starts with some non-negative number d and performs one of the two operations for each i=1,2,…,n, in the increasing order of i.
# The possible operations are:
#
# replace their current number d with d+ai
# replace their current number d with d⊕ai (hereinafter ⊕ denotes the bitwise XOR operation)
# Notice that the chosen operation may be different for different i and for different tellees.
#
# One time, Alice decided to start with d=x and Bob started with d=x+3. Each of them performed fortune telling and got a particular number in the end.
# Notice that the friends chose operations independently of each other, that is, they could apply different operations for the same i.
#
# You learnt that either Alice or Bob ended up with number y in the end, but you don't know whose of the two it was.
# Given the numbers Alice and Bob started with and y, find out who (Alice or Bob) could get the number y after performing the operations.
# It is guaranteed that on the jury tests, exactly one of your friends could have actually gotten that number.

#solution:
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    print("Alice") if ((sum(list(map(int,input().split())))+x+y)%2==0) else print("Bob")