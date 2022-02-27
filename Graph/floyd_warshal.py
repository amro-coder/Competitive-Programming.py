def floyad_warshal():
    for intermediate_node in range(n):
        for parent in range(n):
            for child in range(n):
                distance[parent][child]=min(distance[parent][child],distance[parent][intermediate_node]+distance[intermediate_node][child])
                if(distance[child][child]<0):
                    return False
    return True
n,m=map(int,input().split())
# its easier to represent the graph as a adjacency matrix
# nodes start from zero
graph=[[float("inf")]*n for _ in range(n)]
for _ in range(m):
    a,b,w=map(int,input().split())
    graph[a][b]=graph[b][a]=w
distance=[[float("inf")]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(i==j):
            distance[i][j]=0
        else:
            distance[i][j]=graph[i][j]

print(distance if floyad_warshal() else "graph contains a negtive cycle")

# 5 7
# 0 1 5
# 1 2 2
# 2 3 7
# 3 0 9
# 3 4 2
# 4 0 1
# 1 4 -1