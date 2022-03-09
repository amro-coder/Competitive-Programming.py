# Sam lives in Awesomeburg, its downtown has a triangular shape. Also, the following is true about the triangle:
#
# its vertices have integer coordinates,
# the coordinates of vertices are non-negative, and
# its vertices are not on a single line.
# He calls a point on the downtown's border (that is the border of the triangle) safe if he can reach this point from at least one point of the line y=0 walking along some straight line, without crossing the interior of the triangle.

# Find the total length of the unsafe parts of the downtown border.
# It can be proven that these parts are segments and their number is finite.

# solution:
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    if((y1==y2 and y3<y1) or (y2==y3 and y1<y2) or (y1==y3 and y2<y1)):
        if(y1==y2):
            print(abs(x1-x2))
        elif (y1 == y3):
            print(abs(x1 - x3))
        else:
            print(abs(x2-x3))
    else:
        print(0)



