# There is a sheet of paper that can be represented with a grid of size n×m: n rows and m columns of cells.
# All cells are colored in white initially.
#
# q operations have been applied to the sheet. The i-th of them can be described as follows:
#
# xi yi — choose one of k non-white colors and color the entire row xi and the entire column yi in it.
# The new color is applied to each cell, regardless of whether the cell was colored before the operation.
# The sheet after applying all q operations is called a coloring.
# Two colorings are different if there exists at least one cell that is colored in different colors.
#
# How many different colorings are there? Print the number modulo 998244353.

# solution:
mod=998244353
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,m,k,q=map(int,input().split())
    quieries=[tuple(map(int,input().split())) for _ in range(q)]
    rows = set()
    columns = set()
    quieries.reverse()
    unique=0
    for i in quieries:
        x,y=i
        if(x not in rows or y not in columns):
            unique+=1
            rows.add(x)
            columns.add(y)
        if(len(rows)==n or len(columns)==m):
            break

    print(pow(k,unique,mod))
