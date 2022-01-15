# problem statement
# You are given a tree of n vertices numbered from 1 to n, with edges numbered from 1 to n−1.
# A tree is a connected undirected graph without cycles.
# You have to assign integer weights to each edge of the tree, such that the resultant graph is a prime tree.
# A prime tree is a tree where the weight of every path consisting of one or two edges is prime.
# A path should not visit any vertex twice. The weight of a path is the sum of edge weights on that path.
# Print any valid assignment of weights such that the resultant tree is a prime tree.
# If there is no such assignment, then print −1. It can be proven that if a valid assignment exists, one exists with weights between 1 and 105 as well.

# solution:
import sys
input=sys.stdin.readline
from collections import defaultdict
def addEdgeBothDirections(graph,start,end):
    # going path
    graph[start].append(end)
    # returning path
    graph[end].append(start)
def initalizeNodes(graph,value):
    nodes={}
    for parent,children in graph.items():
        for child in children:
             nodes[parent]=value
             # cause if the edge have a length it will be in form of tuples
             try:
                nodes[child[0]]=value
             except:
                 nodes[child] = value
    return nodes
def DFS(graph,start):
    stack=[]
    stack.append(start)
    nodes=initalizeNodes(graph,False)
    nodes[start]=True
    while stack:
        parent=stack.pop()
        nodes[parent]=True
        for children in graph[parent]:
            if (not nodes[children]):
                stack.append(children)
    return parent
for _ in range(int(input())):
    n=int(input())
    edges=[]
    count=defaultdict(int)
    graph = defaultdict(list)
    value=defaultdict(int)
    maxx=0
    for __ in range(n-1):
        edges.append(tuple(map(int,input().split())))
        addEdgeBothDirections(graph,edges[-1][0],edges[-1][1])
        count[edges[-1][0]]+=1
        count[edges[-1][1]]+=1
        maxx=max(maxx,count[edges[-1][0]],count[edges[-1][1]])
    if(maxx>2):
        print(-1)
    else:
        put=[2,5]
        last=0
        start=DFS(graph,1)
        stack = []
        stack.append(start)
        nodes = initalizeNodes(graph, False)
        nodes[start] = True
        while stack:
            parent = stack.pop()
            nodes[parent] = True
            for children in graph[parent]:
                if (not nodes[children]):
                    stack.append(children)
                    value[(parent,children)]=put[last%2]
                    value[(children,parent)]=put[last%2]
                    last+=1
        ans=[]
        for i in edges:
            ans.append(value[i])
        print(*ans)


