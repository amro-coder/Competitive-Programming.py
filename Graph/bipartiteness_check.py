from collections import deque
def BFS_colouring(start):
    q=deque([start])
    visited[start]=True
    while q:
        parent=q.popleft()
        for child in graph[parent]:
            if (not visited[child]):
                visited[child]=True
                q.append(child)
                colours[child]=not colours[parent]
    return
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
colours=[False]*(n+1)
for i in range(n+1):
    if(not visited[i]):
        BFS_colouring(i)
ans=True
for parent in range(n+1):
    for child in graph[parent]:
        if(not(colours[parent]^colours[child])):
            ans=False
            break
if(ans):
    print("graph is bipartite")
else:
    print("graph is not bipartite")
# input example
# 10 11
# 0 1
# 0 3
# 0 2
# 1 4
# 3 5
# 5 7
# 3 6
# 2 8
# 8 9
# 9 10
# 4 1