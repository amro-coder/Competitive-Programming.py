from collections import deque
def is_bipartite():
    visited = [False] * n
    black = set()
    white = set()
    def BFS_colouring(start):
        q = deque([start])
        visited[start] = True
        black.add(start)
        while q:
            parent = q.popleft()
            for child in graph[parent]:
                if (not visited[child]):
                    visited[child] = True
                    q.append(child)
                    if (parent in black):
                        white.add(child)
                    else:
                        black.add(child)
    for i in range(n):
        if not visited[i]:
            BFS_colouring(i)
    for parent in black:
        for child in graph[parent]:
            if child in black:
                return False,set(),set()
    for parent in white:
        for child in graph[parent]:
            if child in white:
                return False,set(),set()
    return True,black,white

n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans=is_bipartite()
print("graph is not bipartite" if not ans[0] else f"blacks are {ans[1]} and whites are {ans[2]}")


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


