# Alexander is a well-known programmer.
# Today he decided to finally go out and play football, but with the first hit he left a dent on the new Rolls-Royce of the wealthy businessman Big Vova.
# Vladimir has recently opened a store on the popular online marketplace "Zmey-Gorynych", and offers Alex a job: if he shows his programming skills by solving a task, he'll work as a cybersecurity specialist.
# Otherwise, he'll be delivering some doubtful products for the next two years.
#
# You're given n positive integers a1,a2,…,an. Using each of them exactly at once, you're to make such sequence b1,b2,…,bn that sequence c1,c2,…,cn is lexicographically maximal, where ci=GCD(b1,…,bi) - the greatest common divisor of the first i elements of b.
#
# Alexander is really afraid of the conditions of this simple task, so he asks you to solve it.
#
# A sequence a is lexicographically smaller than a sequence b if and only if one of the following holds:
#
# a is a prefix of b, but a≠b;
# in the first position where a and b differ, the sequence a has a smaller element than the corresponding element in b.

# sloution:
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    ans=[]
    accumlated_gcd=0
    for i in range(n):
        index=-1
        value=0
        for j in range(len(x)):
            if(gcd(accumlated_gcd,x[j])>value):
                value=gcd(accumlated_gcd,x[j])
                index=j
        ans.append(x.pop(index))
        accumlated_gcd=value
    print(*ans)
