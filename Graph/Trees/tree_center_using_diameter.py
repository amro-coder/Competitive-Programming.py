from collections import deque
def BFS(start):
    q=deque([start])
    visited[start]=True
    distances[start]=0
    while q:
        parent=q.popleft()
        for child in graph[parent]:
            if (not visited[child]):
                q.append(child)
                visited[child]=True
                distances[child]=distances[parent]+1
                parent_list[child]=parent
    return

# using recursion approach
def dfs(node,parent=-1,length=0):
    parent_list[node]=parent
    global farthest_node,farthest_node_length
    if length>farthest_node_length:
        farthest_node_length=length
        farthest_node=node
    for child in graph[node]:
        if child!=parent:
            dfs(child,node,length+1)

def get_path(node):
    ans=[]
    while(node!=-1):
        ans.append(node)
        node=parent_list[node]
    ans.reverse()
    return ans

n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*n
distances=[-1]*n
parent_list=[-1]*n
BFS(0)# just chooseing an arbitary node
farthest_node=distances.index(max(distances))

visited=[False]*n
distances=[-1]*n
parent_list=[-1]*n
BFS(farthest_node)
tree_diameter=get_path(distances.index(max(distances)))
print(tree_diameter)
if len(tree_diameter)&1:
    print(f"the center of the tree is {tree_diameter[len(tree_diameter)//2]}")
else:
    print(f"both {tree_diameter[len(tree_diameter)//2]} and {tree_diameter[len(tree_diameter)//2-1]} can work as a tree center")


print()
print("using the recursive approach:")
print()
# using recursive approach
farthest_node=0
farthest_node_length=0
parent_list=[-1]*n
dfs(0)

point_a=farthest_node

farthest_node=0
farthest_node_length=0
parent_list=[-1]*n
dfs(point_a)

tree_diameter=get_path(farthest_node)
print(tree_diameter)
if len(tree_diameter)&1:
    print(f"the center of the tree is {tree_diameter[len(tree_diameter)//2]}")
else:
    print(f"both {tree_diameter[len(tree_diameter)//2]} and {tree_diameter[len(tree_diameter)//2-1]} can work as a tree center")




# example for input:
# 9 8
# 0 1
# 0 4
# 1 2
# 1 3
# 3 8
# 4 6
# 4 5
# 5 7

# example for input:(two centers)
# 8 7
# 0 1
# 0 4
# 1 2
# 1 3
# 4 6
# 4 5
# 5 7

