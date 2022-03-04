# we calculate for each node the 2 longest pathes using it's children
# and the calculate the best path using it's parent
# for each node the answer is one of these three pathes
from collections import deque
def bfs(root):
    parent_list=[-1]*n
    ditances=[float("inf")]*n
    queue=deque([root])
    ditances[root]=0
    while(queue):
        parent=queue.popleft()
        for child in graph[parent]:
            if(child!=parent_list[parent]):
                queue.append(child)
                parent_list[child]=parent
                ditances[child]=ditances[parent]+1
    levels=[[] for _ in range(n)]
    for i in range(n):
        levels[ditances[i]].append(i)

    return levels,parent_list

def max_two():
    levels,parent_list=bfs(0) # we choose an arbitary root
    # (value,child_used)
    max_two_lengths=[((0,-1),(0,-1))]*n
    for i in range(n-1,-1,-1):
        for node in levels[i]:
            best_two=[(-1,-1),(-1,-1)]
            for child in graph[node]:
                if child!=parent_list[node]:
                    index=best_two.index(min(best_two))
                    temp=max(max_two_lengths[child])
                    if(temp>best_two[index]):
                        best_two[index]=(temp[0],child)
            best_two.sort(reverse=True)
            if(best_two[0][0]!=-1):
                max_two_lengths[node]=[(best_two[0][0]+1,best_two[0][1]),(best_two[1][0]+1,best_two[1][1])]
    return max_two_lengths,levels,parent_list


def all_longest_pathes():
    max_using_parent=[-1]*n
    max_two_using_child,levels,parent_list=max_two()
    max_using_parent[levels[0][0]]=0 # initalize the parent path using it's parent
    for i in range(1,n):
        for node in levels[i]:
            parent=parent_list[node]
            choice1=max_using_parent[parent] # using the parent from the parent
            choice2=max_two_using_child[parent][0][0] if max_two_using_child[parent][0][1]!=node else max_two_using_child[parent][1][0]
            max_using_parent[node]=max(choice1,choice2)+1

    ans=[-1]*n
    for node in range(n):
        ans[node]=max(max_using_parent[node],max(max_two_using_child[node])[0])
    return ans




n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(all_longest_pathes())

# example input
# 6 5
# 0 1
# 0 2
# 0 3
# 1 4
# 1 5

# example input 2:
# 6 5
# 0 1
# 1 2
# 2 3
# 3 4
# 3 5

# example input 3:
# 8 7
# 0 1
# 0 2
# 0 3
# 3 4
# 3 5
# 1 6
# 6 7
