def DFS(start):
    nodes=edges=0
    stack=[start]
    while stack:
        parent=stack.pop()
        if(not visited[parent]):
            nodes+=1
            visited[parent]=True
            for child in graph[parent]:
                if (not visited[child]):
                    edges+=1
                    stack.append(child)
    return nodes,edges

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)
connected_components=0
for i in range(n+1):
    if(not visited[i]):
        nodes,edges=DFS(i)
        if(edges!=nodes-1):
            print("graph contains at least one cycle")
            break
else:
    print("graph dose not contain any cycle")
# example for input:
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
# 9 4