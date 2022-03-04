# it's a simple traverse but instead of visited we only need to know the parent
# since the node can be visited by only one way
# note that the start of the dfs shapes the tree by becoming the root
# also note that shortest path between two nodes can be found by dfs since its always one path
def dfs(root):
    parent_list=[-1]*n
    queue=[root]
    while(queue):
        parent=queue.pop()
        print(parent)
        # process the parent
        for child in graph[parent]:
            if(child!=parent_list[parent]):
                queue.append(child)
                parent_list[child]=parent
    return parent_list

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
    return ditances

n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(dfs(start))
print(bfs(start))


# example input:
# 7 6 0
# 0 1
# 0 2
# 0 3
# 1 4
# 2 5
# 3 6