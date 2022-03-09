# Consider a grid of size n×n. The rows are numbered top to bottom from 1 to n, the columns are numbered left to right from 1 to n.
#
# The robot is positioned in a cell (1,1). It can perform two types of moves:
#
# D — move one cell down;
# R — move one cell right.
# The robot is not allowed to move outside the grid.
#
# You are given a sequence of moves s — the initial path of the robot. This path doesn't lead the robot outside the grid.
#
# You are allowed to perform an arbitrary number of modifications to it (possibly, zero).
# With one modification, you can duplicate one move in the sequence.
# That is, replace a single occurrence of D with DD or a single occurrence of R with RR.
#
# Count the number of cells such that there exists at least one sequence of modifications that the robot visits this cell on the modified path and doesn't move outside the grid.

# solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    moves=tuple(input().strip())
    discreate_moves=[]
    down=0
    right=0
    for i in moves:
        if i=="D":
            right+=1
            if down:
                discreate_moves.append(down)
            down=0
        else:
            down+=1
            if right:
                discreate_moves.append(right)
            right=0
    if right+down:
        discreate_moves.append(right+down)

    moves_allowed=[n-1-moves.count("R"),n-1-moves.count("D")]
    ans=1
    down=moves[0]=="D"
    if len(discreate_moves)==1:
        ans=n
    else:
        for i in range(len(discreate_moves)):
            ans += discreate_moves[i]
            if i == len(discreate_moves) - 1:
                ans += ((moves_allowed[0] + 1) * (moves_allowed[1] + 1)) - 1
                break
            ans += moves_allowed[down] * discreate_moves[i + 1]
            down^=True

    print(ans)

