# Egor has a table of size n×m, with lines numbered from 1 to n and columns numbered from 1 to m.
# Each cell has a color that can be presented as an integer from 1 to 105.
#
# Let us denote the cell that lies in the intersection of the r-th row and the c-th column as (r,c).
# We define the manhattan distance between two cells (r1,c1) and (r2,c2) as the length of a shortest path between them where each consecutive cells in the path must have a common side.
# The path can go through cells of any color. For example, in the table 3×4 the manhattan distance between (1,2) and (3,3) is 3, one of the shortest paths is the following: (1,2)→(2,2)→(2,3)→(3,3).
#
# Egor decided to calculate the sum of manhattan distances between each pair of cells of the same color. Help him to calculate this sum.
import sys
input= sys.stdin.readline
n,m=map(int,input().split())
x=[]
max_colour=-1
for _ in range(n):
    x.append(tuple(map(int,input().split())))
    for i in x[-1]:
        max_colour=max(max_colour,i)
max_colour+=1
colours=[[[],[]]for _ in range(max_colour)]
for i in range(n):
    for j in range(m):
        colours[x[i][j]-1][0].append(i)

for j in range(m):
    for i in range(n):
        colours[x[i][j]-1][1].append(j)

ans=0
for i in range(max_colour):
    for c in range(2):
        temp=[0]
        for j in range(len(colours[i][c])-1,-1,-1):
            temp.append(temp[-1]+colours[i][c][j])
        temp.reverse()
        temp.pop()
        for j in range(len(temp)-1):
            ans+=temp[j+1]-((len(temp)-1-j)*colours[i][c][j])


print(ans)