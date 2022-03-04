# we want to calculate how many nodes in the subtree of the each node
from collections import deque
def bfs(root):
    parent_list=[-1]*n
    ditances=[float("inf")]*n
    queue=deque([root])
    ditances[root]=0
    while(queue):
        parent=queue.popleft()
        print(parent)
        # process the parent
        for child in graph[parent]:
            if(child!=parent_list[parent]):
                queue.append(child)
                parent_list[child]=parent
                ditances[child]=ditances[parent]+1
    levels=[[] for _ in range(n)]
    for i in range(n):
        levels[ditances[i]].append(i)
    number_of_contained_nodes=[1]*n
    for i in range(n-1,-1,-1):
        for node in levels[i]:
            if parent_list[node]!=-1:
                number_of_contained_nodes[parent_list[node]]+=number_of_contained_nodes[node]
    return number_of_contained_nodes

# lets do it recursively
def dfs_and_count(node,parent=-1):
    for child in graph[node]:
        if(child!=parent):
            dfs_and_count(child,node)
            count[node]+=count[child]
    return

n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(start))
# using the recursive way
count=[1]*n
dfs_and_count(start)
print(count)