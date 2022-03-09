# You are given a tree of n vertices numbered from 1 to n. A tree is a connected undirected graph without cycles.
#
# For each i=1,2,…,n, let wi be the weight of the i-th vertex.
# A vertex is called good if its weight is equal to the sum of the weights of all its neighbors.
#
# Initially, the weights of all nodes are unassigned.
# Assign positive integer weights to each vertex of the tree, such that the number of good vertices in the tree is maximized.
# If there are multiple ways to do it, you have to find one that minimizes the sum of weights of all vertices in the tree.

from collections import deque
def BFS(start):
    parent_list=[-1]*n
    visited = [False] * n
    distances = [False] * n
    q=deque([start])
    visited[start]=True
    distances[start]=0
    while q:
        parent=q.popleft()
        for child in graph[parent]:
            if (not visited[child]):
                visited[child]=True
                q.append(child)
                distances[child]=distances[parent]+1
                parent_list[child]=parent
    levels=[[] for _ in range(n)]
    for i in range(n):
        levels[distances[i]].append(i)
    while not levels[-1]:
        levels.pop()
    return levels,parent_list

import sys
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
if n==2:
    print(2,2)
    print(1,1)
    exit()
dp=[[(),()] for _ in range(n)] # best number of good nodes and best wight for them for the sub tree of node i when node i good and when node i bad
levels,parent_list=BFS(0)
for lev in range(len(levels)-1,-1,-1):
    for node in levels[lev]:
        # if node is taken as a good node
        best_good_nodes=1
        best_weight=len(graph[node])
        for child in graph[node]:
            if child != parent_list[node]:
                best_good_nodes += dp[child][1][0]
                best_weight+=dp[child][1][1]
        dp[node][0]=(best_good_nodes,best_weight)

        # if node is taken as a bad node
        best_good_nodes = 0
        best_weight = 1
        for child in graph[node]:
            if child != parent_list[node]:
                best_choice=max(dp[child],key=lambda a:(a[0],-a[1]))
                best_good_nodes += best_choice[0]
                best_weight += best_choice[1]
        dp[node][1] = (best_good_nodes, best_weight)

# assinging the values of the nodes
good=[False]*n
node_value=[-1]*n
for lev in range(len(levels)):
    for node in levels[lev]:
        if parent_list[node]!=-1 and good[parent_list[node]]:
            # node has to be a bad node since the parent is good
            node_value[node]=1
            good[node]=False
        else:
            good[node]=(dp[node][0][0],-dp[node][0][1])>=(dp[node][1][0],-dp[node][1][1])
            node_value[node]=len(graph[node]) if good[node] else 1

print(*max(dp[0],key=lambda a:(a[0],-a[1])))
print(*node_value)
