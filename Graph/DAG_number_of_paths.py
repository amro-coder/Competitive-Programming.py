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
        for child in graph[parent]:
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


n, m,start = map(int, input().split())
n+=1 # if the first node is one
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [0] * n
topo_sort = []
cycle = False
for node in range(1,n):
    if visited[node] == 0:
        cycle |= dfs(node)
topo_sort.reverse()
print(*topo_sort)
dp=[0]*n
# dp[i] how many ways to reach node i from the start node
# notice if a node a have an edge to node b then the topological sorting will ensure to calculate dp[a] before dp[b].
# which is exactly what we want , we want each node that can reach node i to be calculated before node i.
dp[start]=1
for node in topo_sort:
    for child in graph[node]:
        dp[child]+=dp[node]
print(dp)


# 6 7 1
# 1 2
# 1 4
# 4 5
# 5 2
# 5 3
# 2 3
# 3 6
