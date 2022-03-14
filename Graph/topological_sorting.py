# visited[node]=0 means node is not visited, visited[node]=1 means node is undere processing , visited[node]=2 node is visited
# notice when a node is visited while it's under processing then a cycle must exist
def dfs_recursive(node):
    if visited[node]==1:
        # a cycle exist
        return True
    visited[node]=1
    # node is under processing
    cycle=False
    for child in graph[node]:
        if visited[child]!=2:
            cycle|=dfs_recursive(child)
    visited[node]=2
    topo_sort.append(node)
    return cycle

def dfs(start):
    working_stack=[start]
    while working_stack:
        parent=working_stack[-1]
        if visited[parent]==2:
            working_stack.pop()
            continue
        visited[parent]=1 # node is under processing
        finished=True
        for child in graph[parent]:
            if visited[child]==1:
                return True # a cycle exist
            if (visited[child]!=2):
                finished=False
                working_stack.append(child)
        if finished:
            visited[parent]=2
            working_stack.pop()
            topo_sort.append(parent)
    return False


n,m=map(int,input().split())
# n+=1 # if the first node is one
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
# recursive approach
print("recursive approach")
visited=[0]*n
topo_sort=[]
cycle=False
for node in range(n):
    if visited[node]==0:
        cycle|=dfs_recursive(node)
if cycle:
    print("graph contains a cycle")
else:
    topo_sort.reverse()
    print(*topo_sort)

print()

# itreative approach
print("itreative approach")
visited=[0]*n
topo_sort=[]
cycle=False
for node in range(n):
    if visited[node]==0:
        cycle|=dfs(node)
if cycle:
    print("graph contains a cycle")
else:
    topo_sort.reverse()
    print(*topo_sort)

# example:
# 6 6
# 0 1
# 1 2
# 1 3
# 3 2
# 0 4
# 4 5

# example with a cycle:
# 6 7
# 0 1
# 1 2
# 1 3
# 3 2
# 0 4
# 4 5
# 5 0

# another example:
# 6 5
# 5 0
# 5 2
# 2 3
# 3 1
# 4 0
# 4 1


