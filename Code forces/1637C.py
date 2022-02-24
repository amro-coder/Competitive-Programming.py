# Andrew has n piles with stones. The i-th pile contains ai stones.
# He wants to make his table clean so he decided to put every stone either to the 1-st or the n-th pile.
#
# Andrew can perform the following operation any number of times:
# choose 3 indices 1≤i<j<k≤n, such that the j-th pile contains at least 2 stones, then he takes 2 stones from the pile j and puts one stone into pile i and one stone into pile k.
#
# Tell Andrew what is the minimum number of operations needed to move all the stones to piles 1 and n, or determine if it's impossible.

# solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    needs_one=extra=0
    if(n==3):
        if(x[1]&1):
            print(-1)
        else:
            print(x[1]//2)
    else:
        if(x[1:n-1].count(1)==n-2):
            print(-1)
        else:
            ans=0
            for i in range(1,n-1):
                ans+=(x[i]//2)
                ans+=(x[i]&1)
            print(ans)
