import heapq
n,m=map(int,input().split())
n+=1
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b,w=map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))
queue=[(0,1,-1)] # random node with zero cost and parent -1
visited=[False]*n
min_spaning_tree=[[] for _ in range(n)]
total=0
while queue:
    weight,node,parent=heapq.heappop(queue)
    if not visited[node]:
        visited[node]=True
        total+=weight
        if parent!=-1:
            min_spaning_tree[node].append((weight, parent))
            min_spaning_tree[parent].append((weight, node))
        for child_weight,child in graph[node]:
            heapq.heappush(queue,(child_weight,child,node))
print(total)
print(min_spaning_tree)

# example input:
# 6 8
# 1 2 3
# 1 5 5
# 2 5 6
# 2 3 5
# 5 6 2
# 3 6 3
# 3 4 9
# 6 4 7