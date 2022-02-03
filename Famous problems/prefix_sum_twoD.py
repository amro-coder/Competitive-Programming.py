import itertools
n,m=map(int,input().split())
x=[]
prefix=[[0]*(m+1)]
for _ in range(n):
    x.append(tuple(map(int,input().split())))
    prefix.append([0] + list(itertools.accumulate(x[-1])))
for i in range(1,n+1):
    for j in range(1,m+1):
        prefix[i][j]+=prefix[i-1][j]

for i in prefix:
    print(*i)
for _ in range(int(input())):
    # each point is included in the sum
    p1=tuple(map(int,input().split()))
    p2=tuple(map(int,input().split()))
    p3=tuple(map(int,input().split()))
    p4=tuple(map(int,input().split()))
    print(prefix[p1[0]][p1[1]]+prefix[p4[0]+1][p4[1]+1]-prefix[p2[0]][p2[1]+1]-prefix[p3[0]+1][p3[1]])

