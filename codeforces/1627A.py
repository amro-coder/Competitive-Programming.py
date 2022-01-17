# problem Satement
# There is a grid with n rows and m columns. Some cells are colored black, and the rest of the cells are colored white.
# In one operation, you can select some black cell and do exactly one of the following:
# color all cells in its row black, or
# color all cells in its column black.
# You are given two integers r and c. Find the minimum number of operations required to make the cell in row r and column c black, or determine that it is impossible.

# solution
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,m,r,c=map(int,input().split())
    x=[]
    for __ in range(n):
        x.append(tuple(input().strip()))
    if (x[r - 1][c - 1] == "B"):
        print(0)
    else:
        oneOp=False
        twoOp=False
        for i in range(n):
            for j in range(m):
                if(x[i][j]=="B"):
                    if(i==r-1 or j==c-1):
                        oneOp=True
                    else:
                        twoOp=True
        if(oneOp):
            print(1)
        elif(twoOp):
            print(2)
        else:
            print(-1)
################################

