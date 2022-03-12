def find_parent(x):
    while(x!=parent[x]):
        x=parent[x]
    return x

def unite(x,y):
    parent_x=find_parent(x)
    parent_y=find_parent(y)
    if parent_x!=parent_y:
        if size[parent_x]<size[parent_y]:
            parent_x,parent_y=parent_y,parent_x
#       parent_x has the bigger size
        size[parent_x]+=size[parent_y]
        parent[parent_y]=parent_x
        return True
    # returns false if x and y are in the same set
    return False

n,m=map(int,input().split())
n+=1
edges=[]
for _ in range(m):
    a,b,w=map(int,input().split())
    edges.append((w,a,b))
edges.sort()
parent=[i for i in range(n)]
size=[1]*n
min_spaning_tree=[[] for _ in range(n)]
total=0
for weight,start,end in edges:
    if unite(start,end):
        min_spaning_tree[start].append((weight,end))
        min_spaning_tree[end].append((weight,start))
        total+=weight
print(total)

# example input:
# 6 8
# 1 2 3
# 1 5 5
# 2 5 6
# 2 3 5
# 5 6 2
# 3 6 3
# 3 4 9
# 6 4 7