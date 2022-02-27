# note in an undirected graph if there is a negitive edge then there is a negtive cycle!!
def bellman_ford():
    for _ in range(n-1):
        for start in range(n):
            for weight,end in graph[start]:
                if(distances[start]+weight<distances[end]):
                    distances[end]=distances[start]+weight
                    parent[end]=start
    # checking for a negtive cycle
    for start in range(n):
        for weight, end in graph[start]:
            if distances[start] + weight<distances[end]:
                return False
    return True
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
distances=[float("inf")]*n
distances[start]=0
parent=[-1]*n
print(distances if(bellman_ford()) else "there is a negitive cycle")
print(get_path(n-1))

# 6 7 0
# 0 2 4
# 0 1 3
# 1 3 1
# 3 2 2
# 2 4 7
# 3 5 1
# 5 4 2
