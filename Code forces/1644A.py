# The knight is standing in front of a long and narrow hallway.
#  A princess is waiting at the end of it.
# In a hallway there are three doors: a red door, a green door and a blue door.
#  The doors are placed one after another, however, possibly in a different order.
#  To proceed to the next door, the knight must first open the door before.
# Each door can be only opened with a key of the corresponding color.
#  So three keys: a red key, a green key and a blue key — are also placed somewhere in the hallway.
#  To open the door, the knight should first pick up the key of its color.
# The knight has a map of the hallway.
# r, g, b — denoting red, green and blue keys, respectively.
# Each of these six characters appears in the string exactly once.
# The knight is standing at the beginning of the hallway — on the left on the map.
# Given a map of the hallway, determine if the knight can open all doors and meet the princess at the end of the hallway.
#
#
#
#  solution:

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    string=tuple(input().strip())
    red=0
    green=0
    blue=0
    for i in string:
        if(i=='r'):
            red+=1
        elif(i=='b'):
            blue+=1
        elif(i=='g'):
            green+=1
        elif(i=="R"):
            red-=1
        elif(i=="B"):
            blue-=1
        else:
            green-=1
        if(green<0 or blue<0 or red<0):
            print("NO")
            break
    else:
        print("YES")
