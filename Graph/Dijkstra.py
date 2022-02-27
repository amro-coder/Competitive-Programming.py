# remmeber that an edge with length 2 can be represented as two edges with length 1 and an arbitary node, so that we can use BFS insteas of dijkstra
from heapq import heappop,heappush
def dijkstra(start):
    queue=[(0,start,-1)]
    while(queue):
        weight,next_node,next_node_parent=heappop(queue)
        if(not visited[next_node]):
            visited[next_node]=True
            distances[next_node]=weight
            parent[next_node]=next_node_parent
            for length,child in graph[next_node]:
                heappush(queue,(weight+length,child,next_node))
    return
def get_path(node):
    path=[]
    while(parent[node]!=-1):
        path.append(node)
        node=parent[node]
    path.append(start)
    return list(reversed(path))
n,m,start=map(int,input().split())
# nodes start from zero
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b,w=map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))
visited=[False]*n
distances=[float("inf")]*n
parent=[-1]*n
dijkstra(start)
print(get_path(n-1))

# example input:
# 6 7 0
# 0 2 4
# 0 1 3
# 1 3 1
# 3 2 2
# 2 4 7
# 3 5 1
# 5 4 2