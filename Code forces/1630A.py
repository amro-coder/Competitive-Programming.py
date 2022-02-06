# You are given a set of n (n is always a power of 2) elements containing all integers 0,1,2,…,n−1 exactly once.
# Find n2 pairs of elements such that:
# Each element in the set is in exactly one pair.
# The sum over all pairs of the bitwise AND of its elements must be exactly equal to k.
# Formally, if ai and bi are the elements of the i-th pair, then the following must hold:
# ∑i=1n/2ai&bi=k,
# where & denotes the bitwise AND operation.
# If there are many solutions, print any of them, if there is no solution, print −1 instead.

# solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,k=map(int,input().split())
    if(n==4 and k==3):
        print(-1)
    else:
        ans=[]
        visted=[False]*n
        if(k!=n-1):
            visted[k]=visted[n-1-k]=visted[0]=visted[n-1]=True
            ans.extend([(k,n-1),(0,n-1-k)])
            if(ans[0]==ans[1]):
                ans.pop()
            for i in range(n):
                if(not visted[i]):
                    visted[i]=visted[n-1-i]=True
                    ans.append((i,n-1-i))
        else:
            visted[0] = visted[n-1] = visted[1] = visted[n - 2] =visted[2] = visted[n-3] = True
            ans.extend([(n-2, n - 1), (1, n -3),(0,2)])
            for i in range(n):
                if (not visted[i]):
                    visted[i] = visted[n - 1 - i] = True
                    ans.append((i, n - 1 - i))

            pass
        for i in ans:
            print(*i)