# A binary string is a string that consists of characters 0 and 1.
#
# Let MEX of a binary string be the smallest digit among 0, 1, or 2 that does not occur in the string.
# For example, MEX of 001011 is 2, because 0 and 1 occur in the string at least once, MEX of 1111 is 0, because 0 and 2 do not occur in the string and 0<2.
#
# A binary string s is given.
# You should cut it into any number of substrings such that each character is in exactly one substring.
# It is possible to cut the string into a single substring — the whole string.
#
# A string a is a substring of a string b if
# a can be obtained from b by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.
#
# What is the minimal sum of MEX of all substrings pieces can be?

# solution:
for _ in range(int(input())):
    x=tuple(input())
    ans=0
    check=False
    for i in x:
        if(not check and i=='0'):
            ans+=1
            check=True
        if(i!='0'):
            check=False
        else:
            check=True
    print(min(ans,2))