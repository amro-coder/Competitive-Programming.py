from collections import deque
def BFS(start):
    q=deque([start])
    visited[start]=True
    distances[start]=0
    while q:
        parent=q.popleft()
        for child in graph[parent]:
            if (not visited[child]):
                visited[child]=True
                q.append(child)
                distances[child]=distances[parent]+1
    return
n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
distances=[-1]*(n+1)
BFS(0)
print(*distances)


# example for input:
# 10 10 0
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


