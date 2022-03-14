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


n, m = map(int, input().split())
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
dp=[[float("inf")]*n for _ in range(n)]
# dp[i][j] shortest path from node i to node j
# notice if a node a have an edge to node b then the reversed topological sorting will ensure that dp[b][child] for all b children will be calculated first.
# which is exactly what we want , we want each node that can reach node i to be calculated after i.
for node in range(n):
    dp[node][node]=0
for i in range(n-1,-1,-1):
    for weight,child in graph[topo_sort[i]]:# raching all nodes using this child
        for j in range(i+1,n):
            dp[topo_sort[i]][topo_sort[j]]=min(dp[topo_sort[i]][topo_sort[j]],weight+dp[child][topo_sort[j]])
print(dp)


# 6 7
# 0 2 4
# 0 1 3
# 1 3 1
# 3 2 2
# 2 4 7
# 3 5 1
# 5 4 2
