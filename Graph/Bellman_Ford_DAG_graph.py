# visited[node]=0 means node is not visited, visited[node]=1 means node is undere processing , visited[node]=2 node is visited
# notice when a node is visited while it's under processing then a cycle must exist
def dfs(start):
    working_stack = [start]
    while working_stack:
        parent = working_stack[-1]
        if visited[parent] == 2:
            working_stack.pop()
            continue
        visited[parent] = 1  # node is under processing
        finished = True
        for _,child in graph[parent]:
            if visited[child] == 1:
                return True  # a cycle exist
            if (visited[child] != 2):
                finished = False
                working_stack.append(child)
        if finished:
            visited[parent] = 2
            working_stack.pop()
            topo_sort.append(parent)
    return False

def get_path(node):
    path=[]
    while(parent[node]!=-1):
        path.append(node)
        node=parent[node]
    path.append(start)
    return list(reversed(path))

n, m,start = map(int, input().split())
# n+=1 # if the first node is one
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b,weight = map(int, input().split())
    graph[a].append((weight,b))

visited = [0] * n
topo_sort = []
cycle = False
for node in range(n):
    if visited[node] == 0:
        cycle |= dfs(node)
topo_sort.reverse()
print(*topo_sort)
dp=[float("inf")]*n
# dp[i] shortest path from start to node i
# notice if a node a have an edge to node b then the topological sorting will ensure to calculate dp[a] before dp[b].
# which is exactly what we want , we want each node that can reach node i to be calculated before node i.
dp[start]=0
# creating new graph that only contains the edges used in shortest paths of start node
parent=[-1]*n
for node in topo_sort:
    for weight,child in graph[node]:
        if dp[node]+weight<dp[child]:
            dp[child]=dp[node]+weight
            parent[child]=node
print(dp)

# creating a new graph that only contains the edges needed for the start node to reach all the nodes with the shortest path possiple
new_graph=[[]for _ in range(n)]
for node in range(n):
    if parent[node]!=-1:
        new_graph[parent[node]].append((dp[node]-dp[parent[node]],node))
print(new_graph)


# 6 7 0
# 0 2 4
# 0 1 3
# 1 3 1
# 3 2 2
# 2 4 7
# 3 5 1
# 5 4 2
