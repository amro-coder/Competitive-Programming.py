# problem statement
# Polycarp is very fond of playing the game Minesweeper. Recently he found a similar game and there are such rules.
# There are mines on the field, for each the coordinates of its location are known (xi,yi).
# Each mine has a lifetime in seconds, after which it will explode.
# After the explosion, the mine also detonates all mines vertically and horizontally at a distance of k (two perpendicular lines).
# As a result, we get an explosion on the field in the form of a "plus" symbol ('+'). Thus, one explosion can cause new explosions, and so on.
# Also, Polycarp can detonate anyone mine every second, starting from zero seconds.
# After that, a chain reaction of explosions also takes place.
# Mines explode instantly and also instantly detonate other mines according to the rules described above.
# Polycarp wants to set a new record and asks you to help him calculate in what minimum number of seconds all mines can be detonated

# solution
# 1- using union Find
# def unionFind_initalize(arr):
#     unionFind={}
#     for i in range(len(arr)):
#         unionFind[arr[i]]=[1,arr[i]]
#     return unionFind
#
# def unionFind_find(x,unionFind):
#     while(True):
#         if(unionFind[x][1])==x:
#             return unionFind[x]
#         x=unionFind[x][1]
#
# def unionFind_union(x,y,unionFind):
#     parentx=unionFind_find(x,unionFind)
#     parenty=unionFind_find(y,unionFind)
#     if (parentx==parenty):
#         return
#     size=unionFind[parentx[1]][0]+unionFind[parenty[1]][0]
#     if(parentx<parenty):
#         unionFind[parentx[1]]=[size,unionFind[parenty[1]][1]]
#         unionFind[parenty[1]][0]=size
#     else:
#         unionFind[parenty[1]] =[size,unionFind[parentx[1]][1]]
#         unionFind[parentx[1]][0]=size
#     return
#
# import sys
# input=sys.stdin.readline
# from collections import defaultdict
# for _ in range(int(input())):
#     empty=input()
#     n,k=map(int,input().split())
#     bombs=[]
#     for __ in range(n):
#         bombs.append(tuple(map(int,input().split())))
#     unionfind = unionFind_initalize(bombs)
#
#     bombs.sort()
#     for i in range(n - 1):
#         if (bombs[i][0] == bombs[i + 1][0] and bombs[i + 1][1] <= bombs[i][1] + k):
#             unionFind_union(bombs[i],bombs[i+1],unionfind)
#     bombs.sort(key=lambda a: (a[1], a[0]))
#     for i in range(n - 1):
#         if (bombs[i][1] == bombs[i + 1][1] and bombs[i + 1][0] <= bombs[i][0] + k):
#             unionFind_union(bombs[i],bombs[i+1],unionfind)
#     groups=defaultdict(list)
#     for bomb in bombs:
#         groups[unionFind_find(bomb,unionfind)[1]].append(bomb)
#     groupMin=[]
#     for group in groups.keys():
#         minimum=float('inf')
#         for bomb in groups[group]:
#             minimum=min(minimum,bomb[2])
#         groupMin.append(minimum)
#     groupMin.sort(reverse=True)
#     ans = len(groupMin) - 1
#     for i in range(len(groupMin)):
#         if (groupMin[i] == i):
#             ans = i
#             break
#         elif (groupMin[i] < i):
#             ans = i - 1
#             break
#     print(ans)

# 2- using trees:
import sys
input=sys.stdin.readline
from collections import defaultdict
for _ in range(int(input())):
    empty=input()
    n,k=map(int,input().split())
    bombs=[]
    for __ in range(n):
        bombs.append(tuple(map(int,input().split())))
    tree=defaultdict(list)
    visted=defaultdict(bool)
    bombs.sort()
    for i in range(n-1):
        if(bombs[i][0]==bombs[i+1][0] and bombs[i+1][1]<=bombs[i][1]+k):
            tree[bombs[i]].append(bombs[i+1])
            tree[bombs[i+1]].append(bombs[i])
    bombs.sort(key=lambda a:(a[1],a[0]))
    for i in range(n - 1):
        if (bombs[i][1] == bombs[i + 1][1] and bombs[i + 1][0] <= bombs[i][0] + k):
            tree[bombs[i]].append(bombs[i + 1])
            tree[bombs[i+1]].append(bombs[i])
    groups=[]
    for bomb in bombs:
        minimum=float('inf')
        if(not visted[bomb]):
            queue=[bomb]
            while(queue):
                parent=queue.pop()
                minimum=min(minimum,parent[2])
                visted[parent]=True
                for child in tree[parent]:
                    if (not visted[child]):
                        queue.append(child)
                        visted[child]=True
        if(minimum!=float('inf')):
            groups.append(minimum)
    groups.sort(reverse=True)
    ans=len(groups)-1
    for i in range(len(groups)):
        if(groups[i]==i):
            ans=i
            break
        elif(groups[i]<i):
            ans=i-1
            break
    print(ans)

























