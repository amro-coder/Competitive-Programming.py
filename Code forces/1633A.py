# You are given an integer n.
# You have to change the minimum number of digits in it in such a way that the resulting number does not have any leading zeroes and is divisible by 7.
#
# If there are multiple ways to do it, print any of them. If the given number is already divisible by 7, leave it unchanged.

#solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    if(n%7==0):
        print(n)
    else:
        for i in range((n//10)*10,((n//10)+1)*10+1):
            if(i%7==0):
                print(i)
                break
