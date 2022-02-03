import itertools
x=tuple(map(int,input().split()))
prefix=[0]+list(itertools.accumulate(x))
for _ in range(int(input())):
    # index a is included, index b is not included
    a,b=map(int,input().split())
    print(prefix[b]-prefix[a])
