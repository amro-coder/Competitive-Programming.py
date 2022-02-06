# Recently, the students of School 179 have developed a unique algorithm, which takes in a binary string s as input.
# However, they soon found out that if some substring t of s is a palindrome of length greater than 1, the algorithm will work incorrectly.
# Can the students somehow reorder the characters of s so that the algorithm will work correctly on the string?
#
# A binary string is a string where each character is either 0 or 1.
#
# A string a is a substring of a string b if a can be obtained from b by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.
#
# A palindrome is a string that reads the same backwards as forwards.

#solutiion:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    s=input().strip()
    if(n>2):
        print("NO")
    elif(n==2):
        if(s[0]==s[1]):
            print("NO")
        else:
            print("YES")
    else:
        print("YES")