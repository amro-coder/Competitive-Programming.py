# Wheatley decided to try to make a test chamber.
#  He made a nice test chamber, but there was only one detail absent — cubes.
# For completing the chamber Wheatley needs n cubes.
#  i-th cube has a volume ai.
# Wheatley has to place cubes in such a way that they would be sorted in a non-decreasing order by their volume.
#  Formally, for each i>1, ai−1≤ai must hold.
# To achieve his goal, Wheatley can exchange two neighbouring cubes.
#  It means that for any i>1 you can exchange cubes on positions i−1 and i.
# But there is a problem: Wheatley is very impatient.
#  If Wheatley needs more than n⋅(n−1)/2−1 exchange operations, he won't do this boring work.
# Wheatly wants to know: can cubes be sorted under this conditions?
#
#
#
#  solution:
import sys
from collections import Counter
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    if(x==sorted(x,reverse=True) and max(Counter(x).values())==1):
        print("NO")
    else:
        print("YES")

