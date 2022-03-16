# the idea is the topological sorting for a graph that contains a cycle will never guarantee that last node dose not have an edge to any node.
# But it will always guarantee that the start node will not have any edge entering it except the ones from it's cycle (connected component)
# so for a reverse graph topological ordering will guarantee that connected components will be processed in the right order
# such that each connected component will be processed after processing all connected components that it can reach.
def dfs(start):
    working_stack=[start]
    while working_stack:
        parent=working_stack[-1]
        if visited[parent]==2:
            working_stack.pop()
            continue
        visited[parent]=1 # node is under processing
        finished=True
        for child in reversed_graph[parent]:
            if (visited[child]==0):# child is neither under processing nor visited
                finished=False
                working_stack.append(child)
        if finished:
            visited[parent]=2
            working_stack.pop()
            topo_sort.append(parent)

def dfs_visit(node):
    stack=[node]
    compenent=[]
    while stack:
        parent=stack.pop()
        if not visited[parent]:
            visited[parent]=True
            compenent.append(parent)
            for child in graph[parent]:
                if not visited[child]:
                    stack.append(child)
    return compenent
n,m=map(int,input().split())
# n+=1 # if the first node is one
graph=[[] for _ in range(n)]
reversed_graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    reversed_graph[b].append(a)
# constructing a node ordering from reversed graph
visited=[0]*n
topo_sort=[]
for node in range(n):
    if visited[node]==0:
        dfs(node)
topo_sort.reverse()
# using the order to process each connected component in the right order
visited=[False]*n
strongly_connected_components=[]
for node in topo_sort:
    if not visited[node]:
        strongly_connected_components.append(dfs_visit(node))
print(len(strongly_connected_components))
print(*strongly_connected_components)


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


# 11 18
# 1 3
# 3 5
# 5 1
# 3 11
# 11 6
# 11 8
# 6 10
# 10 8
# 8 6
# 5 9
# 5 7
# 7 9
# 9 4
# 4 7
# 9 2
# 2 4
# 2 10
# 9 8

